# Generated by Django 2.2.6 on 2019-11-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0031_auto_20191108_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='features',
            field=models.ManyToManyField(blank=True, to='hospedajes_app.Feature'),
        ),
    ]
