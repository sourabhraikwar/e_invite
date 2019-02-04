from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from .forms import *
from django.http import HttpResponse
from .models import *
from dashboard.models import addCards
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
	cards_data = addCards.objects.all()
	context = {
		'title': 'Home',
		'cards_data': cards_data
	}
	return render(request, 'invi_cards/home.html', context)

def aboutUs(request):
	context = {
		'title': 'Aboutus'
	}
	return render(request, 'invi_cards/About.html', context)

def contactUs(request):
	context = {
		'title': 'Contatus'
	}
	return render(request, 'invi_cards/Contact.html', context)


def reset(request):
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
	if request.method == 'POST':
		form = Signup_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/login/')
	else:
		form = Signup_form()
	return render(request, 'registration/signup.html', {'form': form})

def card(request):
	return render(request, 'invi_cards/card.html')
