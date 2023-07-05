from django.urls import path
from telegramemail.views import send_emails, my_view
from telegramemail import views


app_name = 'telegramemail'
urlpatterns = [
    path('send_email/', send_emails, name='send_email'),
    path('my_view/', my_view, name='my_view'),
]