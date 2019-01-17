# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse,HttpResponseRedirect
=======
<<<<<<< HEAD
from django.conf import settings
from django.http import HttpResponse
from .forms import *

=======
from django.http import HttpResponse,HttpResponseRedirect
>>>>>>> cd0e2f6d1434a0d90f3cbab716bf8fb6ddd64331
>>>>>>> 5b80aebf576827e9c2ff9635c18807b2dc448ed7
import pyglet
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):

	context = {
		'title': 'Home'
	}

	return render(request, 'home.html', context)


def Forms(request):
	form = E_Form()
	return render (request, 'home.html', {'form': form})

frame = 0
def on_draw(request):

    pyglet.image.get_buffer_manager().get_color_buffer().save(str(frame)+'.png')
    return render(request, 'home.html')


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
