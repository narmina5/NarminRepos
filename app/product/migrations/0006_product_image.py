# Generated by Django 4.2.7 on 2023-12-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_brand_product_brand"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(null=True, upload_to="products"),
        ),
    ]
