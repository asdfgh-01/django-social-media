# Generated by Django 4.1.7 on 2023-03-25 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_message_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
