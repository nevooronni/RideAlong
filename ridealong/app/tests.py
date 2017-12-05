from django.test import TestCase
from .models import Driver,Rider

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