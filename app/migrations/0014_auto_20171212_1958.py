# Generated by Django 2.0 on 2017-12-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20171212_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='car_pic',
            field=models.ImageField(blank=True, default='car_pic/default_car.jpg', upload_to='car_pic'),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='prof_pic',
            field=models.ImageField(blank=True, default='Driver/prof_pic/prof_pic.png', upload_to='Driver/prof_pic'),
        ),
        migrations.AlterField(
            model_name='riderprofile',
            name='prof_pic',
            field=models.ImageField(blank=True, default='Rider/prof_pic/prof_pic.png', upload_to='Rider/prof_pic'),
        ),
    ]