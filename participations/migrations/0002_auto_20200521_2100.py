# Generated by Django 3.0.6 on 2020-05-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='answer',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('MAYBE', 'Peut-être')], max_length=5),
        ),
    ]
