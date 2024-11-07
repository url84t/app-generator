# Generated by Django 4.2.8 on 2024-11-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0060_alter_products_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="card_info",
            field=models.CharField(default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="products",
            name="design_css",
            field=models.CharField(
                choices=[
                    ("NA", "NA"),
                    ("bootstrap", "bootstrap"),
                    ("bootstrap4", "bootstrap4"),
                    ("bootstrap5", "bootstrap5"),
                    ("tailwind", "tailwind"),
                    ("mui", "mui"),
                ],
                default="NA",
                max_length=24,
            ),
        ),
    ]