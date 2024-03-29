# Generated by Django 4.2.7 on 2023-11-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("is_parent", models.BooleanField(default=False)),
                ("child", models.ManyToManyField(blank=True, to="product.category")),
            ],
            options={"verbose_name": "Category", "verbose_name_plural": "Categories",},
        ),
    ]
