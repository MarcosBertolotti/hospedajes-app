# Generated by Django 2.2.6 on 2019-11-07 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0018_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='features',
            field=models.ManyToManyField(null=True, to='hospedajes_app.Feature'),
        ),
    ]
