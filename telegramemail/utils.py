from django.core.mail import send_mail


def send_notification_email(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=None,  # It will use the DEFAULT_FROM_EMAIL setting
        recipient_list=recipient_list,
        fail_silently=False,
    )