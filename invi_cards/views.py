# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import *


# Create your views here.
def home(request):

	context = {
		'title': 'Home'
	}

	return render(request, 'home.html', context)


def Forms(request):
	form = E_Form()
	return render (request, 'home.html', {'form': form})

