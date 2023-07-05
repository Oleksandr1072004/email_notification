from django.core.mail import EmailMessage
from telegram_django_project.settings import *
import telebot

bot = telebot.TeleBot('1893106887:AAG2wMuW1kl0w4Zar-F03NBXx6nfbqCNmiY')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Extract message text from the Telegram message
    text = message.text

    # Create an EmailMessage object
    email = EmailMessage(
        'Subject',
        text,
        EMAIL_HOST_USER,
        [RECIPIENT_LIST[0], RECIPIENT_LIST[-1]],
        headers={'Message-ID': 'foo'},
    )

    # Send the email
    email.send()


def main():
    bot.polling()


if __name__ == '__main__':
    main()