# Generated by Django 4.2.13 on 2024-05-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2_app', '0007_rename_messages_notification_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_loggedin',
            field=models.BooleanField(default=False),
        ),
    ]