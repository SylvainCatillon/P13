# Generated by Django 3.0.6 on 2020-05-18 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plannings', '0004_auto_20200516_1924'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GuestMail',
            new_name='GuestEmail',
        ),
        migrations.RenameField(
            model_name='planning',
            old_name='guest_mails',
            new_name='guest_emails',
        ),
    ]