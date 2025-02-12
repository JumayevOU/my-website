# Generated by Django 5.1.1 on 2024-10-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=202)),
                ('image', models.ImageField(upload_to='collection/')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
