# Generated by Django 2.1.5 on 2020-04-14 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='products',
        ),
    ]
