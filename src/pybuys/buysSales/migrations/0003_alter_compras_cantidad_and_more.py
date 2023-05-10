# Generated by Django 4.1.8 on 2023-05-09 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buysSales", "0002_alter_compras_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="compras",
            name="cantidad",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="productosencarrito",
            name="cantidad",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="ventas",
            name="cantidad",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
