# Generated by Django 3.0.6 on 2020-05-16 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plannings', '0003_auto_20200516_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planning_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
