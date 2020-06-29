# Generated by Django 3.0.7 on 2020-06-29 01:48

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20200627_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='valid_from_dt_tm',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='valid_until_dt_tm',
            field=models.DateTimeField(default=datetime.datetime(2150, 12, 31, 0, 0)),
        ),
    ]