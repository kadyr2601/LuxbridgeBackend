# Generated by Django 5.2.3 on 2025-06-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_service_card_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqs',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='faqs',
            name='title',
        ),
        migrations.AddField(
            model_name='faqs',
            name='answer',
            field=models.TextField(default=1, verbose_name='FAQ answer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faqs',
            name='question',
            field=models.CharField(default=1, max_length=256, verbose_name='FAQ question'),
            preserve_default=False,
        ),
    ]
