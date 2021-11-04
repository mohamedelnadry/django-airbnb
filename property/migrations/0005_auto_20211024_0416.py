# Generated by Django 3.2.8 on 2021-10-24 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20211024_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyform',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='propertyform',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]