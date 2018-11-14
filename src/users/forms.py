from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email= forms.EmailField()
	first_name = forms.CharField(max_length = 30, label="First Name")
	last_name = forms.CharField(max_length = 30, label="Last Name")

	def names(self, request, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return user


	class Meta:
		model = User #class shows all the fields in this order in the form
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User #class shows all the fields in this order in the form
		fields = ['email']



class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile #class shows all the fields in this order in the form
		fields = ['image']

