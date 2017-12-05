from django import forms 
from .models import Driver

class DriverRegistrationForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields = ('first_name', 'last_name','email','phone','city')	