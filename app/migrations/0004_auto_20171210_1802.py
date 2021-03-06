# Generated by Django 2.0 on 2017-12-10 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171206_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_pic', models.ImageField(blank=True, default='DRIVER_PIC', upload_to='driver/profile_pic')),
                ('gender', models.TextField(blank=True, choices=[('F', 'female'), ('M', 'male'), ('Both', 'both'), ('None', 'non-specified')], default='None', max_length=50)),
                ('car_pic', models.ImageField(blank=True, default='CAR_PIC', upload_to='car_pic')),
                ('car_plate', models.TextField(blank=True, max_length=255)),
                ('car_color', models.TextField(blank=True, max_length=255)),
                ('car_capacity', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='driver',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rider',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rider',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rider',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rider',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Driver'),
        ),
    ]
