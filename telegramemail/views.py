from bottle import Bottle, response, request as bottle_request
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler
from .models import EmailMessage
from telegram_django_project.settings import EMAIL_HOST_USER
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from telegram_django_project import settings
from ipware.ip import get_client_ip
from .tasks import send_email, send_telegram_message
from .utils import send_notification_email
from aiogram import Bot, Dispatcher, executor, types
import telegram, requests, telebot


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, dict):
            return str(obj)
        return super().default(obj)


def bot(request, msg, my_chat_id, my_token):
    bot = telegram.Bot(token=my_token)
    bot.sendMessage(chat_id=my_chat_id, text=msg)


@csrf_exempt
def send_emails(request):
    # Telegram bot webhook endpoint
    token = '1893106887:AAG2wMuW1kl0w4Zar-F03NBXx6nfbqCNmiY'
    # bot = telegram.Bot(token)
    # updater = Bot(token)
    # dp = Dispatcher(updater)
    recipient_of_email = ''
    subject_of_email = ''
    body_of_email = ''

    def start(update: Update, context):
        update.message.reply_text('Welcome to the bot!')

    def send_mails(update: Update, context):
        email_messages = EmailMessage.objects.all()
        for message in email_messages:
            send_email(
                EmailMessage.recipient.split(','),
                EmailMessage.subject,
                EmailMessage.body,
                fail_silently=False,
            )
        update.message.reply_text('Emails sent successfully!')

    telegrambot = telebot.TeleBot(token)

    @telegrambot.message_handler(commands=['start'])
    def start(message):
        telegrambot.send_message(message.chat.id, 'It works!')

    @telegrambot.message_handler(commands=['fill','create'])
    def fill_email(message):
        msg = telegrambot.send_message(message.chat.id, "Subject: ")
        # if (msg.from_user.first_name == message.from_user.first_name and msg.from_user.last_name == message.from_user.last_name) or:
        telegrambot.register_next_step_handler(msg, process_fill_email_body)

    def process_fill_email_body(message):
        global subject_of_email
        subject_of_email = message.text
        chat_id = message.chat.id
        EmailMessage.subject = subject_of_email
        msg = telegrambot.send_message(chat_id, "Body of email:")
        telegrambot.register_next_step_handler(msg, process_fill_email_recipient)

    def process_fill_email_recipient(message):
        global body_of_email
        body_of_email = message.text
        EmailMessage.body = body_of_email
        chat_id = message.chat.id
        msg = telegrambot.send_message(chat_id, "Which emails do you want to recipient?")
        telegrambot.register_next_step_handler(msg, finish_process_filling_email)

    def finish_process_filling_email(message):
        global recipient_of_email
        if "@gmail.com" in message.text:
            recipient_of_email = message.text
            EmailMessage.recipient = recipient_of_email
            chat_id = message.chat.id
            telegrambot.send_message(chat_id, "Thanks for your filling "
                                                      "to send emails! :)")

    text = f"Email recipient: {EmailMessage.recipient}\nSubject: {EmailMessage.subject}\nBody: {EmailMessage.body}"

    @telegrambot.message_handler(commands=['text'])
    def send_Message(message):
        nonlocal text
        telegrambot.send_message(message.chat.id, text)

    # start_handler = CommandHandler('start', start)
    # send_email_handler = CommandHandler('sendemail', send_mails)
    @telegrambot.message_handler(commands=['send'])
    def send_email_from_telegram(message):
        telegrambot.send_message(message.chat.id, "Sending to email\n\n\nPlease wait!")
        send_mail(EmailMessage.subject, EmailMessage.body, EMAIL_HOST_USER, [EmailMessage.recipient])
        telegrambot.send_message(message.chat.id, "It's sending in email successfully")

    # updater.start_polling()
    telegrambot.polling()

    return HttpResponse('Telegram bot webhook endpoint')