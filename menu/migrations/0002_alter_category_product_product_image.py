# Generated by Django 5.1.6 on 2025-03-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_product',
            name='product_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
