# Generated by Django 5.2.3 on 2025-06-15 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_alter_property_location_alter_property_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=512, verbose_name='Property Name'),
        ),
    ]
