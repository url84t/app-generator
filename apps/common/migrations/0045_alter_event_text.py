# Generated by Django 4.2.8 on 2024-10-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0044_alter_products_tech1_alter_products_tech2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="text",
            field=models.TextField(blank=True, null=True),
        ),
    ]