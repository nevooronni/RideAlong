from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

DRIVER_PIC = ""
CAR_PIC = ""

class Rider(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	username = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.IntegerField()
	city = models.CharField(max_length = 30)
	password = models.CharField(max_length=50)
	
	@classmethod
	def riders_list(cls):
		riders = Rider.objects.all()
		return riders

class DriverProfile():
	driver = models.OneToOneField(Driver,on_delete=models.CASCADE)
	prof_pic = models.ImageField(blank=True,upload_to="",default="DRIVER_PIC")
	gender = models.CharField(max_length=30,choices=Gender_Choices,default='None',blank=True)
	car_pic = models.ImageField(blank=True,upload_to="",default="CAR_PIC")
	car_plate = models.CharField(blank=True,max_length=255)
	car_color = models.CharField(max_length=255,blank=True)
	car_capacity = models.PostitiveIntegerField(default=0,blank=True)

	def __str__(self):
		return self.driver.first_name + '' + self.driver.last_name

	@classmethod
	def get_profiles(cls):
		driver_profiles = DriverProfile.objects.all()
		return driver_profiles

	@receiver(post_save,sender=Driver)#create profile when creating driver
	def create_profile(sender,instance,created,**kwargs):
		if created:
			DriverProfile.objects.create(driver=instance)

	@receiver(post_save,sender=Driver)#save deriver proflie when creating driver
	def save_profile(sender,instance,**kwargs):
		instance.driverprofile.save()


class Driver(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.IntegerField()
	city = models.CharField(max_length = 30)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name + '' + self.last_name

	@classmethod
	def drivers_list(cls):
		drivers = Driver.objects.all()
		return drivers



