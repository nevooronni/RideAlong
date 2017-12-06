from django.db import models


class Rider(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.IntegerField()
	city = models.CharField(max_length = 30)
	password = models.CharField(max_length=50)
	
	@classmethod
	def riders_list(cls):
		riders = Rider.objects.all()
		return riders

# class RiderProfile():

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

