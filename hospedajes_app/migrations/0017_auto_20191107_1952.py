# Generated by Django 2.2.6 on 2019-11-07 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0016_auto_20191107_0604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentaldate',
            old_name='fk_booking',
            new_name='booking',
        ),
        migrations.RenameField(
            model_name='rentaldate',
            old_name='fk_property',
            new_name='property',
        ),
    ]