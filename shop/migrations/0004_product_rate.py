# Generated by Django 5.1.1 on 2024-10-07 17:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_product_sale_product_sale_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="rate",
            field=models.IntegerField(
                blank=True,
                default=0,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]
