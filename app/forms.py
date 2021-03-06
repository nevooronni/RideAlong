from django import forms 
from .models import Driver,Rider,DriverProfile,RiderProfile,DriverReview,RiderReview,DriverJourney

class RiderRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:	
		model = Rider
		fields = ('first_name','last_name','password','email','phone','city',)

class DriverRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Driver
		fields = ('first_name','last_name','password','email','phone','city',)	

class DriverLoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta :
		model = Driver
		fields = ('email','password',)

class RiderLoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)	
	class Meta:
		model = Rider
		fields = ('email','password',)

class EditDriverProfileForm(forms.ModelForm):
	class Meta:
		model = DriverProfile
		fields = ('prof_pic','gender','car_pic','car_plate','car_color','car_capacity','email',)

class EditRiderProfileForm(forms.ModelForm):
	class Meta:
		model = RiderProfile
		fields = ('prof_pic','gender','email','general_location',)

class DriverReviewForm(forms.ModelForm):
	class Meta:
		model = DriverReview
		fields = ('review',)

class RiderReviewForm(forms.ModelForm):
	class Meta:
		models = RiderReview
		fields = ('review',)

class DriverJourneyForm(forms.ModelForm):
	class Meta:
		model = DriverJourney
		fields = ('current_location','destination',)
