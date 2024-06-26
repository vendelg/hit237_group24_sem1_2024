# Generated by Django 4.2.13 on 2024-05-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2_app', '0017_project_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='message',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_approved',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
