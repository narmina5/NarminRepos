# Generated by Django 4.2.7 on 2023-12-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0006_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True),
        ),
    ]
