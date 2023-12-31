# Generated by Django 4.2.6 on 2023-12-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaintingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description of the painting')),
                ('size', models.CharField(max_length=20, verbose_name='Size of the painting')),
                ('custom_size', models.CharField(blank=True, help_text='Specify the size if not in the list', max_length=50, null=True, verbose_name='Custom size')),
                ('add_signature', models.BooleanField(default=True, verbose_name='Add artist signature')),
                ('examples', models.FileField(blank=True, null=True, upload_to='painting_examples/', verbose_name='File with examples')),
            ],
        ),
    ]
