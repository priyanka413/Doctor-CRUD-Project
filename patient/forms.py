from django.core import validators
from django import forms
from .models import User


class PatientRegistration(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'address']
		widgets = {
		'name': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'address': forms.TextInput(attrs={'class':'form-control'}),
		}