# Generated by Django 3.2.18 on 2023-06-12 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatrooms',
            name='user',
        ),
    ]