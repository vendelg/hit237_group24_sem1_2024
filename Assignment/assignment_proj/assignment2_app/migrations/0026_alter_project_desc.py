# Generated by Django 5.0.5 on 2024-05-29 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2_app', '0025_alter_project_tid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='desc',
            field=models.TextField(max_length=1500),
        ),
    ]