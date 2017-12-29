from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DriverRegistrationForm,DriverLoginForm,RiderRegistrationForm,RiderLoginForm,EditDriverProfileForm,EditRiderProfileForm,DriverJourneyForm
from .models import Rider,Driver,DriverProfile,RiderProfile,DriverJourney,BookDriver
from django.http import Http404,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

def index(request):
	return render(request, 'all-app/index.html')

def register_driver(request):
	if request.method == 'POST':
		form = DriverRegistrationForm(request.POST)

		if form.is_valid:
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			password = request.POST.get('password')
			email = request.POST.get('email')
			phone = request.POST.get('phone')
			city = request.POST.get('city')
			new_driver = Driver(first_name=first_name,last_name=last_name,password=password,phone=phone,city=city)
			new_driver.save()
			return redirect(login_driver)
		else:
			messages.error(request,('Please correct the error below.'))
	
	else:

		form = DriverRegistrationForm()

		return render(request,'registration/driver/driver_registration.html',{"form":form})	

def login_driver(request):
	if request.method == 'POST':

		form = DriverLoginForm(request.POST)

		if form.is_valid():
			password = request.POST.get('password')

			try:
				specific_driver = Driver.objects.get(password=password)
				return redirect(driver,specific_driver.id)

			except ObjectDoesNotExist:
				raise Http404()

		else:
			messages.error(request,('please enter the correct login details'))

	else:
		form = DriverLoginForm()

		return render(request,'registration/driver/driver_login.html',{"form":form})

def page(request):
	return render(request,'all-app/page.html')

def driver(request,id):
	drivers = Driver.objects.all()

	try:
		driver = Driver.objects.get(id=id)

		if driver in drivers:
			driver_profile = DriverProfile.objects.get(driver=driver)
			
			return render(request,'driver/profile.html',{"driver":driver,"driver_profile":driver_profile})
		else:
			return redirect(login_driver)

	except ObjectDoesNotExist:
		return redirect(register_driver)

@transaction.atomic
def edit_driver_profile(request,id): 
	drivers = Driver.objects.all()

	try:
		specific_driver = Driver.objects.get(id=id)

		if specific_driver in drivers:
			if request.method == 'POST':
				edit_profile_form = EditDriverProfileForm(request.POST,instance=specific_driver.driverprofile,files=request.FILES)

				if edit_profile_form.is_valid():
					driver_profile = edit_profile_form.save(commit=False)
					driver_profile.driver = specific_driver
					driver_profile.prof_pic = edit_profile_form.cleaned_data['prof_pic']
					driver_profile.car_pic = edit_profile_form.cleaned_data['car_pic']
					driver_profile.car_plate = edit_profile_form.cleaned_data['car_plate']
					driver_profile.car_capacity = edit_profile_form.cleaned_data['car_capacity']
					driver_profile.car_color = edit_profile_form.cleaned_data['car_color']
					driver_profile.email = edit_profile_form.cleaned_data['email']
					driver_profile.save()

					return redirect(driver, specific_driver.id)
				else:
					messages.error(request,('please correct the error below.'))

			else:
				edit_profile_form = EditDriverProfileForm(instance=specific_driver.driverprofile)
				return render(request, 'driver/edit_profile.html',{"driver":specific_driver,"edit_profile_form":edit_profile_form})

		else:
			return redirect(login_driver)

	except ObjectDoesNotExist:
		return redirect(register_driver)
					
def register_rider(request):
	if request.method == 'POST':
		form = RiderRegistrationForm(request.POST)

		if form.is_valid:
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			password = request.POST.get('password')
			email = request.POST.get('email')
			phone = request.POST.get('phone')
			city = request.POST.get('city')
			new_rider = Rider(first_name=first_name,last_name=last_name,password=password,phone=phone,city=city)
			new_rider.save()
			return redirect(login_rider)
		else:
			messages.error(request,('Please correct the error below.'))
	
	else:

		form = RiderRegistrationForm()

		return render(request,'registration/rider/rider_registration.html',{"form":form})	

def login_rider(request):
	if request.method == 'POST':

		form = RiderLoginForm(request.POST)

		if form.is_valid():
			password = request.POST.get('password')

			try:
				specific_rider = Rider.objects.get(password=password)
				return redirect(rider,specific_rider.id)

			except ObjectDoesNotExist:
				raise Http404()

		else:
			messages.error(request,('please enter the correct login details'))

	else:
		form = RiderLoginForm()

		return render(request,'registration/rider/rider_login.html',{"form":form})

def rider(request,id):
	riders = Rider.objects.all()

	try:
		rider = Rider.objects.get(id=id)

		if rider in riders:
			rider_profile = RiderProfile.objects.get(rider=rider)
			
			return render(request,'rider/profile.html',{"rider":rider,"rider_profile":rider_profile})
		else:
			return redirect(login_rider)

	except ObjectDoesNotExist:
		return redirect(register_rider)

@transaction.atomic
def edit_rider_profile(request,id): 
	riders = Rider.objects.all()

	try:
		specific_rider = Rider.objects.get(id=id)

		if specific_rider in riders:
			if request.method == 'POST':
				edit_profile_form = EditRiderProfileForm(request.POST,instance=specific_rider.riderprofile,files=request.FILES)

				if edit_profile_form.is_valid():
					rider_profile = edit_profile_form.save(commit=False)
					rider_profile.rider = specific_rider
					rider_profile.prof_pic = edit_profile_form.cleaned_data['prof_pic']
					rider_profile.email = edit_profile_form.cleaned_data['email']
					rider_profile.general_location = edit_profile_form.cleaned_data['general_location']
					rider_profile.save()

					return redirect(rider, specific_rider.id)
				else:
					messages.error(request,('please correct the error below.'))

			else:
				edit_profile_form = EditRiderProfileForm(instance=specific_rider.riderprofile)
				return render(request, 'rider/edit_profile.html',{"rider":specific_rider,"edit_profile_form":edit_profile_form})

		else:
			return redirect(login_rider)

	except ObjectDoesNotExist:
		return redirect(register_rider)

def create_journey(request,driverprofile_id):
	try:
		driver_profile = DriverProfile.objects.get(id=driverprofile_id)

		specific_driver = driver_profile.driver

		drivers = Driver.objects.all()

		if specific_driver in drivers:

			if request.method == 'POST':

				form = DriverJourneyForm(request.POST)

				if form.is_valid:

					create_journey = form.save(commit=False)
					create_journey.driver_profile = driver_profile
					create_journey.save()
					return redirect(drive, specific_driver.id)
					
				else:
					messages.error(request,('please enter the right information below'))

			else:
				form = DriverJourneyForm()

				return render(request,'driver/create_journey.html',{"form":form,"driver":specific_driver})	

		else:
			return redirect(login_driver)

	except ObjectDoesNotExist:
		return redirect(register_driver)

def drive(request,driver_id):
	drivers = Driver.objects.all()

	try:
		driver = Driver.objects.get(id=driver_id)

		if driver in drivers:
			driver_profile = driver.driverprofile
			journeys = DriverJourney.objects.filter(driver_profile=driver_profile)
			return render(request, 'driver/drive.html',{"driver":driver,"journeys":journeys,"driver_profile":driver_profile})
		else:
			return redirect(driver_login)

	except ObjectDoesNotExist:
		return redirect(register_driver)		
	
def nearby_drivers(request,rider_id):
	riders = Rider.objects.all()

	try:
		rider = Rider.objects.get(id=rider_id)

		if rider in riders:
			rider_profile = RiderProfile.objects.get(rider=rider_id)
			rider_location = rider_profile.general_location
			driver_journeys = DriverJourney.objects.all()
			nearby_drivers = DriverJourney.nearby_drivers(rider_location)

			if len(nearby_drivers) == 0:
				location = rider_location
				return render(request,'rider/nearby_drivers.html',{"rider":rider,"location":location})
			else:
				return render(request,'rider/nearby_drivers.html',{"nearby_drivers":nearby_drivers,"rider":rider})
		else:
			return redirect(login_rider)

	except ObjectDoesNotExist:
		return redirect(register_rider)	

def request_ride(request,rider_id,driver_journey_id):
	riders = Rider.objects.all()

	try:
		requesting_rider = Rider.objects.get(id=rider_id)	

		if requesting_rider in riders:
			rider_profile = requesting_rider.riderprofile
			driver_journey = DriverJourney.objects.get(id=driver_journey_id)
			current_bookings = BookDriver.objects.filter(driver_journey=driver_journey.id)

			if len(current_bookings) < driver_journey.driver_profile.car_capacity:
				seats_left = driver_journey.driver_profile.car_capacity - len(current_bookings)
				return render(request, 'rider/request_ride.html', {"rider":requesting_rider,"driver_journey":driver_journey,"seats_left":seats_left})

			elif len(current_bookings) == driver_journey.driver_profile.car_capacity:
				message = 'This car is fully booked'
				return render(request, 'rider/request_ride.html', {"rider":requesting_rider,"driver_journey":driver_journeys,"message":message,"seats":driver_journey.driver_profile.car_capacity})	

		else:
			return redirect(rider_login)

	except ObjectDoesNotExist:
		return redirect(register_rider)
