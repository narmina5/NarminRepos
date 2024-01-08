# Generated by Django 4.2.7 on 2023-12-28 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("subtotal", models.DecimalField(decimal_places=2, max_digits=16)),
                ("total", models.DecimalField(decimal_places=2, max_digits=16)),
                ("shipping", models.DecimalField(decimal_places=2, max_digits=16)),
                ("is_done", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Order", "verbose_name_plural": "Orders",},
        ),
    ]
