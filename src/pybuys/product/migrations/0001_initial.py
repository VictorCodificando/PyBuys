# Generated by Django 4.1.8 on 2023-04-27 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Caracteristicas",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("descripcion", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Categorias",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=40)),
                (
                    "grupo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.categorias",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Productos",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=50)),
                ("precio", models.FloatField()),
                ("foto", models.CharField(max_length=50)),
                ("rebaja", models.FloatField()),
                ("cantidad", models.IntegerField()),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.categorias",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CaracteristicaPorProducto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "caracteristica_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.caracteristicas",
                    ),
                ),
                (
                    "producto_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.productos",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="caracteristicaporproducto",
            constraint=models.UniqueConstraint(
                fields=("caracteristica_id", "producto_id"), name="unique_caract_prod"
            ),
        ),
    ]