# Generated by Django 4.2.6 on 2023-12-11 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paintingrequest',
            name='custom_size',
        ),
    ]
