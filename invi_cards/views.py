# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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

frame = 0
def on_draw(request):
    pyglet.image.get_buffer_manager().get_color_buffer().save(str(frame)+'.png')
    return render(request, 'home.html')

def reset(request):
	if request.method == 'POST':
		form = Login_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			
			try:
			    u = User.objects.get(username=username)
			except User.DoesNotExist:
			    u = None
			if u:
				u.set_password('')
				u.save()
				return HttpResponse('Reset Successfully')
	else:
		form = Login_form()
	return render(request, 'registration/password_reset_form.html', {'form':form})