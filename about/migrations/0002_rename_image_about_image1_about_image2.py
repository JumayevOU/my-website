# Generated by Django 5.1.1 on 2024-10-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='about',
            name='image2',
            field=models.ImageField(default='images/default.jpg', upload_to='about/'),
            preserve_default=False,
        ),
    ]
