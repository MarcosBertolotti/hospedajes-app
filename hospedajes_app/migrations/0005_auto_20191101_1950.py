# Generated by Django 2.2.6 on 2019-11-01 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0004_auto_20191101_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='fk_city',
        ),
        migrations.RemoveField(
            model_name='property',
            name='fk_user',
        ),
    ]
