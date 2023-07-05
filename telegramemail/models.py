from django.db import models


class EmailMessage(models.Model):
    subject = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True)
    recipient = models.EmailField(null=True, blank=True)