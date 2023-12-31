# Generated by Django 3.2.7 on 2023-06-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegramemail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
