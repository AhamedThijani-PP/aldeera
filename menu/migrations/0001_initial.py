# Generated by Django 5.1.6 on 2025-03-15 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('new_arrival', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
            ],
        ),
        migrations.CreateModel(
            name='category_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('new_arrival', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
            ],
        ),
    ]
