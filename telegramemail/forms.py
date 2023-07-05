# base/forms.py
from telegram_django_bot import forms as td_forms

class BotMenuElemForm(td_forms.TelegramModelForm):
    class Meta:
        model = BotMenuElem
        fields = ['command', "is_visable", "callbacks_db", "message", "buttons_db"]
