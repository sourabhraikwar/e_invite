from django.urls import path
from .views import *

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path('users', usersList, name='userslist'),
	path('cards', cardsList, name='cardslist'),
	path('emails', emails, name='emails'),
	path('settings', settings, name='settings'),
	path('profile', profile, name='profile'),
]