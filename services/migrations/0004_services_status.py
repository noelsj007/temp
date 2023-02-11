# Generated by Django 4.0.5 on 2023-02-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_serviceprovider_service_provider_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('deleted', 'deleted')], default='active', max_length=20),
        ),
    ]