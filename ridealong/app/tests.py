from django.test import TestCase
from .models import Driver,Rider,DriverProfile,RiderProfile,RiderReview

class DriverTestClass(TestCase):
	'''
	test for driver class
	'''
	def setUp(self):
		'''
		setup method
		'''
		self.driver = Driver(first_name = "Neville",last_name = "Oronni",email = "nevooronni@gmail.com",phone = "0799244265",city = "Nairobi")

	def test_drivers_list(self):
		'''
		test to see if you can get drivers list
		'''
		all_drivers = Driver.drivers_list()
		drivers = Driver.objects.all()

		self.assertTrue(len(all_drivers) == len(drivers))

class DriverProfileTestClass(TestCase):
	'''
	test for driver profile class
	'''
	def setUp(self):
		'''
		setup method
		'''
		self.profile = DriverProfile(gender='male',car_plate='KAV4718',car_color='black',car_capacity=4)

	def test_instance(self):
		'''
		check if profile is an instance of the driver profile class
		'''
		self.assertTrue(isinstance(self.profile,DriverProfile))

	def test_drivers_profile_list(self):
		'''
		get list of drivers profiles from the db and return a list
		'''
		list_of_drivers_profiles = DriverProfile.driver_profile_list()
		driver_profiles = DriverProfile.objects.all()
		self.assertTrue(len(list_of_drivers_profiles) == len(driver_profiles))

class RiderTestClass(TestCase):
	'''
	test for rider class
	'''
	def setUp(self):
		'''
		set up method
		'''
		self.rider = Rider(first_name = "Neville",last_name = "Oronni",email = "nevooronni@gmail.com",phone = "0704569516",city = "Nairobi")

	def test_riders_list(self):
		'''
		test to see if you can get the riders list
		'''
		all_riders = Rider.riders_list()
		riders = Rider.objects.all()

		self.assertTrue(len(all_riders) == len(riders))

class RiderProfileTestClass(TestCase):
	'''
	test for rider profile class
	'''
	def setUp(self):
		'''
		set up method create an instance of driver profile class
		'''
		self.profile = RiderProfile(gender='male',home_address='pangani')

	def test_instance(self):
		'''
		test to check if rider profiles is an instance of rider class
		'''
		self.assertTrue(isinstance(self.profile,RiderProfile))

	def test_rider_profile_list(self):
		'''
		test to see if you can get rider profile from the db
		'''
		list_of_riders_profiles = RiderProfile.riders_profile_list()
		rider_profiles = RiderProfile.objects.all()
		self.assertTrue(len(list_of_riders_profiles) == len(rider_profiles))

class RiderReviewTestClass(TestCase):
	'''
	test for the rider review class
	'''
	def setUp(self):
		'''
		set up method to create an instance of the RiderReview class
		'''
		self.review = RiderReview(review='not bad for first ride would be willing to try again.')

	def test_instance(self):
		'''
		test to check if the rider reveiw is an instance of the RiderReview class
		'''
		self.assertTrue(isinstance(self.review,RiderReview))

	def test_rider_reviews(self):
		'''
		test to get list of rider reviews form the db
		'''
		self.driver = Driver(first_name = "Neville",last_name = "Oronni",email = "nevooronni@gmail.com",phone = "0799244265",city = "Nairobi")
		self.driver.save()

		self.rider = Rider(first_name = "chelsea",last_name = "obrien",email = "chelseaobrien@gmail.com",phone = "0725459516",city = "Nairobi")
		self.rider.save()

		self.rider_profile = RiderProfile(rider=self.rider,gender="female",home_address="Nairobi")
		self.rider_review = RiderReview(driver=self.driver,rider_profile=self.rider_profile,review="this was a good ride")

		all_reviews = RiderReview.all_rider_reviews(self.rider_profile.id)
		rider_reviews = RiderReview.objects.all()

		self.assertTrue(len(all_reviews) == len(rider_reviews))