# Generated by Django 4.2.7 on 2024-01-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0015_product_adding_to_basket_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="logo",
            field=models.FileField(blank=True, null=True, upload_to="brands"),
        ),
    ]
