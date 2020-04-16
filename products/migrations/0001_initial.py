# Generated by Django 2.1.5 on 2020-03-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=20000)),
                ('description', models.TextField(default='')),
                ('req', models.TextField(default='')),
                ('category', models.ManyToManyField(to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(to='products.Sub_category'),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(to='products.Sub_category'),
        ),
    ]