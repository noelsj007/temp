# Generated by Django 4.0.5 on 2023-02-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provider_name', models.CharField(max_length=50)),
                ('contact', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='media/uploads/service_image/')),
                ('video', models.FileField(blank=True, upload_to='media/uploads/service_video/')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
