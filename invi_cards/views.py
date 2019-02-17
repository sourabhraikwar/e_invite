from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *
# Create your views here.

def home(request):
	"""
	Home page defined here

	"""
	context = {
		'title': 'Home',
	}
	
	return render(request, 'invi_cards/home.html', context)

def reset(request):
	"""
	Reset Password Defined here

	Modules in use:

	* Login_form from invi_cards.forms
	"""
	usr_err=""
	if request.method == 'POST':
		form = Login_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			
			try:
			    u = User.objects.get(username=username)
			except User.DoesNotExist:
			    u = None
			    usr_err = "Username not exist"
			if u:
				u.set_password('1234')
				u.save()
				return HttpResponseRedirect('/accounts/login/')
	else:
		form = Login_form()

	context = {
		'form':form,
		'usr_err': usr_err,
	}
	return render(request, 'registration/password_reset_form.html', context)

def signup(request):
	"""
	Signup or Create new account method defined here

	Modules in use:

	* Signup_form from invi_cards.forms

	"""
	if request.method == 'POST':
		form = Signup_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/login/')
	else:
		form = Signup_form()
	return render(request, 'registration/signup.html', {'form': form})

