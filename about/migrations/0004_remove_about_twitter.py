# Generated by Django 5.1.1 on 2024-10-08 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='twitter',
        ),
    ]
