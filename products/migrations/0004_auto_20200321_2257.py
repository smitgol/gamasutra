# Generated by Django 2.1.5 on 2020-03-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200321_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(default='', upload_to='products'),
        ),
    ]