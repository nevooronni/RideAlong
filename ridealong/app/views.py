from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DriverRegistrationForm,DriverLoginForm
from .models import Rider,Driver
from django.http import Http404,JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	return render(request, 'all-app/index.html')

def register_driver(request):
	if request.method == 'POST':
		form = DriverRegistrationForm(request.POST)

		if form.is_valid:
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			phone = request.POST.get('phone')
			city = request.POST.get('city')
			new_driver = Driver(first_name=first_name,last_name=last_name,phone=phone,city=city)
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
			phone = request.POST.get('phone')

			try:
				specific_driver = Driver.objects.get(phone=phone)
				return redirect(driver, specific_driver.id)

			except ObjectDoesNotExist:
				raise Http404()

		else:
			messages.error(request,('please enter the correct login details'))

	else:
		form = DriverLoginForm()

		return render(request,'registration/driver/driver_login.html',{"form":form})

def page(request):
	return render(request,'all-app/page.html')


@login_required(login_url='/new/driver')
def driver(request,id):
	specific_driver = Driver.objects.get(id=id)
	# driver_profile = DriverProfile.objects.get(driver=unique_driver)

	return render(request,'driver/profile.html',{"driver":specific_driver})




