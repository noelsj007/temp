# Generated by Django 4.0.5 on 2023-01-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30, null=True)),
                ('mail', models.EmailField(max_length=100)),
                ('msg_subject', models.CharField(max_length=30)),
                ('msg_content', models.TextField(blank=True)),
            ],
        ),
    ]
