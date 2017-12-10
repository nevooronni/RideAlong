from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

DRIVER_PIC = "Driver/profile_pic/"
CAR_PIC = "car_pic/"

Genders_Choices = (
		('F', 'female'),
		('M', 'male'),
		('Both', 'both'),
		('None', 'non-specified'),
	)

class Rider(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	phone = models.IntegerField()
	city = models.CharField(max_length = 50)
	password = models.CharField(max_length=50)
	
	@classmethod
	def riders_list(cls):
		riders = Rider.objects.all()
		return riders

class Driver(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	phone = models.IntegerField()
	city = models.CharField(max_length = 50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name + '' + self.last_name

	@classmethod
	def drivers_list(cls):
		drivers = Driver.objects.all()
		return drivers

class DriverProfile(models.Model):
	driver = models.OneToOneField(Driver,on_delete=models.CASCADE)
	prof_pic = models.ImageField(blank=True,upload_to="driver/profile_pic",default="DRIVER_PIC")
	gender = models.TextField(max_length=50,choices=Genders_Choices,default='None',blank=True)
	car_pic = models.ImageField(blank=True,upload_to="car_pic",default="CAR_PIC")
	car_plate = models.TextField(max_length=255,blank=True)
	car_color = models.TextField(max_length=255,blank=True)
	car_capacity = models.PositiveIntegerField(default=0,blank=True)

	def __str__(self):
		return self.driver.first_name + '' + self.driver.last_name

	@classmethod
	def driver_profile_list(cls):
		driver_profiles = DriverProfile.objects.all()
		return driver_profiles

	# @receiver(post_save,sender=Driver)#create profile when creating driver
	# def create_profile(sender,instance,created,**kwargs):
	# 	if created:
	# 		DriverProfile.objects.create(driver=instance)

	# @receiver(post_save,sender=Driver)#save deriver proflie when creating driver
	# def save_profile(sender,instance,**kwargs):
	# 	instance.driverprofile.save()




