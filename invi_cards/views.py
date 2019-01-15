# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
<<<<<<< HEAD
from django.conf import settings
from django.http import HttpResponse
from .forms import *

=======
from django.http import HttpResponse
import pyglet
>>>>>>> 95e19f66841b216605e776625f6bdb43784f678f

# Create your views here.
def home(request):

	context = {
		'title': 'Home'
	}

	return render(request, 'home.html', context)

<<<<<<< HEAD

def Forms(request):
	form = E_Form()
	return render (request, 'home.html', {'form': form})

=======
frame = 0
def on_draw(request):

    pyglet.image.get_buffer_manager().get_color_buffer().save(str(frame)+'.png')
    return render(request, 'home.html')
>>>>>>> 95e19f66841b216605e776625f6bdb43784f678f
