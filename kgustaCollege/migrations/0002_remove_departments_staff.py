# Generated by Django 3.1 on 2021-03-29 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kgustaCollege', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='staff',
        ),
    ]