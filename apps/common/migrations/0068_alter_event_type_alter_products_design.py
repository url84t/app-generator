# Generated by Django 4.2.8 on 2024-12-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0067_delete_apikey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    ("GENERAL", "General"),
                    ("ERR_500", "ERR_500"),
                    ("ERR_404", "ERR_404"),
                    ("ERR_403", "ERR_403"),
                    ("ERR_400", "ERR_400"),
                    ("API", "API"),
                ],
                default="GENERAL",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="design",
            field=models.CharField(
                choices=[
                    ("NA", "NA"),
                    ("rocket", "rocket"),
                    ("rocket-pro", "rocket-pro"),
                    ("rocket-ecommerce", "rocket-ecommerce"),
                    ("datta-able", "datta-able"),
                    ("datta-able-pro", "datta-able-pro"),
                    ("gradient-able", "gradient-able"),
                    ("gradient-able-pro", "gradient-able-pro"),
                    ("berry-dashboard", "berry-dashboard"),
                    ("berry-dashboard-pro", "berry-dashboard-pro"),
                    ("volt-dashboard", "volt-dashboard"),
                    ("volt-dashboard-pro", "volt-dashboard-pro"),
                    ("soft-ui-dashboard", "soft-ui-dashboard"),
                    ("soft-ui-dashboard-pro", "soft-ui-dashboard-pro"),
                    ("material-dashboard", "material-dashboard"),
                    ("material-dashboard-pro", "material-dashboard-pro"),
                    ("material-dashboard2-pro", "material-dashboard2-pro"),
                    ("corporate-dashboard", "corporate-dashboard"),
                    ("corporate-dashboard-pro", "corporate-dashboard-pro"),
                    ("argon-dashboard", "argon-dashboard"),
                    ("argon-dashboard-pro", "argon-dashboard-pro"),
                    ("argon-dashboard2-pro", "argon-dashboard2-pro"),
                    ("black-dashboard", "black-dashboard"),
                    ("black-dashboard-pro", "black-dashboard-pro"),
                    ("modernize-dashboard", "modernize-dashboard"),
                    ("modernize-dashboard-pro", "modernize-dashboard-pro"),
                    ("adminlte", "adminlte"),
                    ("adminlte-pro", "adminlte-pro"),
                    ("atlantis-dark", "atlantis-dark"),
                    ("atlantis-dark-pro", "atlantis-dark-pro"),
                    ("tabler", "tabler"),
                    ("coreui", "coreui"),
                    ("coreui-pro", "coreui-pro"),
                    ("material-kit", "material-kit"),
                    ("material-kit-pro", "material-kit-pro"),
                    ("argon-design", "argon-design"),
                    ("argon-design-pro", "argon-design-pro"),
                    ("pixel-bootstrap", "pixel-bootstrap"),
                    ("pixel-bootstrap-pro", "pixel-bootstrap-pro"),
                    ("soft-ui-design", "soft-ui-design"),
                    ("soft-ui-design-pro", "soft-ui-design-pro"),
                    ("bootstrap-design", "bootstrap-design"),
                    ("flowbite", "flowbite"),
                    ("tailwind", "tailwind"),
                    ("mui", "mui"),
                    ("shadcn", "shadcn"),
                    ("bulma", "bulma"),
                    ("pure-css", "pure-css"),
                ],
                default="NA",
                max_length=24,
            ),
        ),
    ]
