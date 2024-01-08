# Generated by Django 4.2.7 on 2023-11-25 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_remove_color_product_type_remove_size_product_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
            ],
            options={"verbose_name": "Brand", "verbose_name_plural": "Brands",},
        ),
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="product.brand",
            ),
        ),
    ]