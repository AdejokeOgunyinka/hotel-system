# Generated by Django 3.1.7 on 2021-02-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20210228_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]