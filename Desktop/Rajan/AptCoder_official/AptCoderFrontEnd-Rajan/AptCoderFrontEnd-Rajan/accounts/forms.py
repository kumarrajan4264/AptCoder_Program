from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Course_Registration,UserModel,InformationModel


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		
class InformationForm(forms.ModelForm):
	class Meta:
		model = InformationModel
		fields = ['first_name','last_name','address','contact_number']
