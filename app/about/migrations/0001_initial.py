# Generated by Django 4.2.7 on 2023-11-06 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="about")),
            ],
            options={
                "verbose_name": "Haqqimizda",
                "verbose_name_plural": "Haqqimizda",
            },
        ),
        migrations.CreateModel(
            name="AboutPoint",
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
                ("text", models.CharField(max_length=255)),
                (
                    "about",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="points",
                        to="about.about",
                    ),
                ),
            ],
            options={
                "verbose_name": "Haqqimizda punktu",
                "verbose_name_plural": "Haqqimizda punktlari",
            },
        ),
    ]
