# Generated by Django 4.1.8 on 2023-05-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_alter_productos_descripcion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productos",
            name="rebaja",
            field=models.FloatField(default=0, null=True),
        ),
    ]
