# Generated by Django 5.0 on 2024-01-06 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_appoint'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appoint',
        ),
    ]