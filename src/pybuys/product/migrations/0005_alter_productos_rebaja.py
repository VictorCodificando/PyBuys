# Generated by Django 4.1.8 on 2023-05-22 17:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_productos_precio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productos",
            name="rebaja",
            field=models.FloatField(
                default=0,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]