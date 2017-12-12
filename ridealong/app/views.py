from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DriverRegistrationForm,DriverLoginForm,RiderRegistrationForm,RiderLoginForm,EditDriverProfileForm
from .models import Rider,Driver,DriverProfile,RiderProfile
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

@login_required(login_url='/new/rider')
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
	

