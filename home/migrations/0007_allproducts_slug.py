# Generated by Django 4.0 on 2022-02-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_allproducts_product_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproducts',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
