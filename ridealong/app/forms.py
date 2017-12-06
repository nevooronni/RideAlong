from django import forms 
from .models import Driver,Rider

class RiderRegistrationForm(forms.ModelForm):
	class Meta:	
		model = Rider
		fields = ('first_name','last_name','email','phone','city',)

class DriverRegistrationForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields = ('first_name','last_name','email','phone','city',)	

class DriverLoginForm(forms.ModelForm):
	class Meta :
		model = Driver
		fields = ('phone',)

class RiderLoginForm(forms.ModelForm):
	class Meta:
		model = Rider
		fields = ('phone',)

# class EditDriverProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = DriverProfile
# 		fields = ('')

# class EditRiderProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = RiderProfile
# 		fields = ('')
