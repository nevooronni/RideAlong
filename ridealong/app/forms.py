from django import forms 
from .models import Driver,Rider

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
		fields = ('phone','password')

class RiderLoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)	
	class Meta:
		model = Rider
		fields = ('phone','password')

# class EditDriverProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = DriverProfile
# 		fields = ('')

# class EditRiderProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = RiderProfile
# 		fields = ('')
