from django.contrib import admin
from .models import EmailMessage
from .tasks import send_email,send_telegram_message
from .utils import send_notification_email
from django.core.mail import send_mail
from telegram_django_project.settings import EMAIL_HOST_USER, RECIPIENT_LIST


# Register your models here.
class EmailMessageAdmin(admin.ModelAdmin):
    # ...
    # def save_model(self, request, obj, form, change):
    #     # Perform any custom logic or operations before saving the model
    #     # For example, you can send an email notification when a model is saved
    #     self.send_email_notification(obj, 'saved')
    #
    #     # Call the super method to continue with the default save_model behavior
    #     super().save_model(request, obj, form, change)
    #
    # def delete_model(self, request, obj):
    #     # Perform any custom logic or operations before deleting the model
    #     # For example, you can send an email notification when a model is deleted
    #     self.send_email_notification(obj, 'deleted')
    #
    #     # Call the super method to continue with the default delete_model behavior
    #     super().delete_model(request, obj)
    #
    # def send_email_notification(self, obj, action):
    #     #subject = f'{action.capitalize()} {obj} in the admin'
    #     #message = f'The model {obj} was {action} in the admin.'
    #     #recipient_list = [YourModel.sent_email]
    #
    #     email = EmailMessage(YourModel.subject, YourModel.message, YourModel.email, YourModel.sent_email)
    #     email.send()

    def save(self, *args, **kwargs):
        # ... your save logic ...

        # Send email notification
        subject = 'Notification'
        message = 'Hello, a notification email has been sent.'
        recipient_list = ['recipient1@example.com', 'recipient2@example.com']
        # send_email(EmailMessage.recipient.split(','), EmailMessage.subject, EmailMessage.body)
        # send_telegram_message(EmailMessage.subject, EmailMessage.body, EmailMessage.recipient.split(','))
        # send_notification_email(EmailMessage.subject, EmailMessage.body,
        #                         EmailMessage.recipient.split(','))
        send_mail(EmailMessage.subject, EmailMessage.body,
                  EMAIL_HOST_USER,
                  [recipient for recipient in RECIPIENT_LIST])

        super().save(*args, **kwargs)


# admin.site.register(EmailMessage)
# admin.site.register(EmailMessageAdmin)
admin.site.register(EmailMessage, EmailMessageAdmin)