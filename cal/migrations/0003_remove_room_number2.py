# Generated by Django 3.0.7 on 2020-06-26 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_auto_20200626_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='number2',
        ),
    ]
