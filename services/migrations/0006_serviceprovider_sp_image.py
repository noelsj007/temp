# Generated by Django 4.1.6 on 2023-02-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0005_serviceprovider_star"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceprovider",
            name="sp_image",
            field=models.ImageField(
                blank=True, upload_to="media/uploads/service_provider_image/"
            ),
        ),
    ]
