# Generated by Django 4.1.7 on 2023-05-28 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_message_user_alter_room_host_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
