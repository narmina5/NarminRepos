# Generated by Django 4.2.7 on 2024-01-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0016_brand_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="categories"),
        ),
    ]