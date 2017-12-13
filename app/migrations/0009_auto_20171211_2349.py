# Generated by Django 2.0 on 2017-12-11 20:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20171211_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverprofile',
            name='email',
            field=models.EmailField(default=datetime.datetime(2017, 12, 11, 20, 49, 13, 906473, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='car_color',
            field=models.TextField(blank=True, default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='car_plate',
            field=models.TextField(blank=True, default='None', max_length=255),
        ),
    ]