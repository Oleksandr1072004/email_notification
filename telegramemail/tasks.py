from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from celery import shared_task
from telegram import Bot
from telegram_django_project.settings import TELEGRAM_BOT_TOKEN,EMAIL_HOST_USER
import string, telebot


@shared_task
def send_email(recipient, subject, message):
    send_mail(subject, message, EMAIL_HOST_USER, [recipient])


@shared_task
def send_telegram_message(message):
    bot_token = TELEGRAM_BOT_TOKEN
    bot = telebot.TeleBot(token=bot_token)
    bot.send_message(message.chat_id, text=message)