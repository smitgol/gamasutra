# Generated by Django 2.1.5 on 2020-04-08 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='wish_item',
            new_name='wished_item',
        ),
    ]
