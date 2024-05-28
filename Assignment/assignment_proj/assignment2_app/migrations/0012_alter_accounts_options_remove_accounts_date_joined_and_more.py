# Generated by Django 4.2.13 on 2024-05-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2_app', '0011_alter_accounts_options_accounts_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounts',
            options={},
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='role',
            field=models.CharField(choices=[('COORDINATOR', 'Coordinator'), ('STUDENT', 'Student'), ('SUPERVISOR', 'Supervisor')], max_length=50),
        ),
    ]