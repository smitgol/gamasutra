# Generated by Django 2.1.5 on 2020-04-11 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200408_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wished_item',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
