# Generated by Django 3.2.7 on 2021-09-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
