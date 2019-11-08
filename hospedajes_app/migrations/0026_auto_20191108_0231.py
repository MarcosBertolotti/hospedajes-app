# Generated by Django 2.2.6 on 2019-11-08 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0025_auto_20191108_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='booking',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospedajes_app.Profile'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospedajes_app.City'),
        ),
        migrations.AlterField(
            model_name='property',
            name='daily_import',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='pax',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospedajes_app.Host'),
        ),
        migrations.AlterField(
            model_name='rentaldate',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rentaldate',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospedajes_app.Property'),
        ),
    ]