# Generated by Django 4.2.7 on 2024-01-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0014_product_has_discount_product_old_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="adding_to_basket_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
