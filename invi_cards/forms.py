<<<<<<< HEAD
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
=======
<<<<<<< HEAD
from django import forms
>>>>>>> 5b80aebf576827e9c2ff9635c18807b2dc448ed7

class E_Form(forms.Form):
    
    title = forms.CharField(label='Enter the title', min_length=100, max_length=150)
    Firstname = forms.CharField(label='Enter firstname', min_length=40, max_length=50)
    Secondname = forms.CharField(label='Enter Secondname', min_length=40, max_length=50)
<<<<<<< HEAD

class Login_form(forms.Form):
	username = forms.CharField(max_length=20)

class Signup_form(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
=======
=======
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class Login_form(forms.Form):
	username = forms.CharField(max_length=20)
	
>>>>>>> cd0e2f6d1434a0d90f3cbab716bf8fb6ddd64331
>>>>>>> 5b80aebf576827e9c2ff9635c18807b2dc448ed7
