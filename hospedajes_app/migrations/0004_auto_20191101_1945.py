# Generated by Django 2.2.6 on 2019-11-01 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0003_auto_20191101_1940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Bookings'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterModelOptions(
            name='rentaldate',
            options={'verbose_name_plural': 'RentalDates'},
        ),
    ]
