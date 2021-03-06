from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

Genders_Choices = (
		('Female', 'female'),
		('Male', 'male'),
		('Both', 'both'),
		('None', 'non-specified'),
	)


class Rider(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField()
	phone = models.PositiveIntegerField()
	city = models.CharField(max_length = 30)
	password = models.CharField(max_length=30)
	
	@classmethod
	def riders_list(cls):
		riders = Rider.objects.all()
		return riders

class RiderProfile(models.Model):
	rider = models.OneToOneField(Rider,on_delete=models.CASCADE)
	prof_pic = models.ImageField(blank=True,upload_to='Rider/prof_pic',default="Rider/prof_pic/prof_pic.png")
	email = models.EmailField()
	gender = models.CharField(max_length=30,choices=Genders_Choices,default='None',blank=True)
	general_location = models.CharField(blank=True,max_length=255)

	def __str__(self):
		return self.rider.first_name + '' + self.rider.last_name	

	@classmethod
	def riders_profile_list(cls):
		riders_profiles = Driver.objects.all()
		return riders_profiles

	@receiver(post_save,sender=Rider)
	def create_profile(sender,instance,created,**kwargs):
		if created:
			RiderProfile.objects.create(rider=instance)

	@receiver(post_save,sender=Rider)
	def save_profile(sender,instance,**kwargs):
		instance.riderprofile.save()


class Driver(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.IntegerField()
	city = models.CharField(max_length = 50)
	password = models.CharField(max_length=30)

	def __str__(self):
		return self.first_name + '' + self.last_name

	@classmethod
	def drivers_list(cls):
		drivers = Rider.objects.all()
		return drivers

class DriverProfile(models.Model):
	driver = models.OneToOneField(Driver,on_delete=models.CASCADE)
	prof_pic = models.ImageField(blank=True,upload_to="Driver/prof_pic",default="Driver/prof_pic/prof_pic.png")
	gender = models.TextField(max_length=50,choices=Genders_Choices,default='None',blank=True)
	car_pic = models.ImageField(blank=True,upload_to="car_pic",default="car_pic/default_car.jpg")
	email = models.EmailField() 
	car_plate = models.CharField(max_length=255,blank=True,default='None')
	car_color = models.CharField(max_length=255,blank=True,default='None')
	car_capacity = models.PositiveIntegerField(default=0,blank=True)

	def __str__(self):
		return self.driver.first_name + '' + self.driver.last_name

	@classmethod
	def driver_profile_list(cls):
		driver_profiles = DriverProfile.objects.all()
		return driver_profiles

	@receiver(post_save,sender=Driver)#create profile when creating driver
	def create_profile(sender,instance,created,**kwargs):
		if created:
			DriverProfile.objects.create(driver=instance)

	@receiver(post_save,sender=Driver)#save deriver proflie when creating driver
	def save_profile(sender,instance,**kwargs):
		instance.driverprofile.save()

class RiderReview(models.Model):
	driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
	rider_profile = models.ForeignKey(RiderProfile,on_delete=models.CASCADE)
	review = models.TextField()

	def __str__(self):
		return self.driver.first_name + '' + self.driver.last_name

	@classmethod
	def all_rider_reviews(self,rider_profile_id):
		rider_reviews =RiderReview.objects.filter(rider_profile=rider_profile_id)
		return rider_reviews


class DriverReview(models.Model):
	rider = models.ForeignKey(Rider,on_delete=models.CASCADE)
	driver_profile = models.ForeignKey(DriverProfile,on_delete=models.CASCADE)
	review = models.TextField()

	def __str__(self):
		return self.rider.first_name + '' + self.rider.last_name

	@classmethod
	def all_driver_reviews(self,driver_profile_id):
		driver_reviews = DriverReview.objects.filter(driver_profile=driver_profile_id)
		return driver_reviews

class DriverJourney(models.Model):
	driver_profile = models.ForeignKey(DriverProfile,on_delete=models.CASCADE)
	current_location = models.CharField(max_length = 255)
	destination = models.CharField(max_length = 255)
	time = models.DateTimeField(auto_now_add = True, null = True)

	class Meta:
		ordering = ['-time']#order in ascending order


	def __str__(self):
		return self.driver_profile.first_name + '' + self.driver_profile.last_name

	@classmethod
	def nearby_drivers(cls,rider_location):
		nearby_drivers = DriverJourney.objects.filter(current_location__icontains=rider_location)#serch for a match		
		return nearby_drivers

class BookDriver(models.Model):
	rider_profile = models.ForeignKey(RiderProfile,on_delete = models.CASCADE)
	driver_journey = models.ForeignKey(DriverJourney,on_delete = models.CASCADE)

	def __str__(self):
		return self.rider_profile.first_name + '' + self.rider_profile.last_name