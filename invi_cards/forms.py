from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class Login_form(forms.Form):
	username = forms.CharField(max_length=20)
	