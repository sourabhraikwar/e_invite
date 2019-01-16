from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class E_Form(forms.Form):
    
    title = forms.CharField(label='Enter the title', min_length=100, max_length=150)
    Firstname = forms.CharField(label='Enter firstname', min_length=40, max_length=50)
    Secondname = forms.CharField(label='Enter Secondname', min_length=40, max_length=50)

class Login_form(forms.Form):
	username = forms.CharField(max_length=20)

class Signup_form(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
