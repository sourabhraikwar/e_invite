from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):

	context = {
		'title': 'Dashboard'
	}
	return render(request, 'dashboard/dashboard.html', context)

def usersList(request):

	context = {
		'title': 'Users List'
	}
	return render(request, 'dashboard/users-list.html', context)

def cardsList(request):

	context = {
		'title': 'Cards List'
	}
	return render(request, 'dashboard/cards-list.html', context)

def emails(request):

	context = {
		'title': 'Cards List'
	}
	return render(request, 'dashboard/emails.html', context)

def settings(request):

	context = {
		'title': 'Settings'
	}
	return render(request, 'dashboard/settings.html', context)

def profile(request):

	context = {
		'title': 'Profile'
	}
	return render(request, 'dashboard/profile.html', context)
