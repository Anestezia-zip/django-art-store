# Generated by Django 4.1 on 2023-12-26 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_rating_productrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrating',
            name='rating',
        ),
        migrations.AddField(
            model_name='productrating',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]