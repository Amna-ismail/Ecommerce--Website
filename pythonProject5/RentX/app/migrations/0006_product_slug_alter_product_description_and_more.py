# Generated by Django 4.2.8 on 2023-12-29 23:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_section_product_image_product_section_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_information',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterModelTable(
            name='product',
            table='app_Product',
        ),
    ]
