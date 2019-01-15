# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import *

import pyglet

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
