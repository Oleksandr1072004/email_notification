# Generated by Django 4.2.2 on 2023-07-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegramemail', '0005_auto_20230620_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='recipient',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
