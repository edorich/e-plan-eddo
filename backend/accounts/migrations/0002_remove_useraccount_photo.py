# Generated by Django 4.0.10 on 2023-02-21 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='photo',
        ),
    ]
