# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
<<<<<<< HEAD
from django.conf import settings
from django.http import HttpResponse
from .forms import *

=======
from django.http import HttpResponse,HttpResponseRedirect
>>>>>>> cd0e2f6d1434a0d90f3cbab716bf8fb6ddd64331
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