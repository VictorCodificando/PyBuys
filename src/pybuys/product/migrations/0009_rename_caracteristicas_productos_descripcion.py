# Generated by Django 4.1.8 on 2023-04-29 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0008_remove_productos_caracteristicas_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productos",
            old_name="caracteristicas",
            new_name="descripcion",
        ),
    ]
