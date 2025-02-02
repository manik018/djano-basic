# Generated by Django 5.1.5 on 2025-01-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firts_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images')),
                ('designation', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
