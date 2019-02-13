from django.urls import path
from .views import *

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path('users', usersList, name='userslist'),
	path('emails', emails, name='emails'),
	path('settings', settings, name='settings'),
	path('profile', profile, name='profile'),
	path('wedding-cards', weddingCardsList, name='wedding'),
	path('birthday-cards', birthdayCardsList, name='birthday'),
	path('inauguration-cards', inaugurationcardsList, name='inauguration'),
	path('edit_card/<int:id>', editCard, name='edit_card'),
	path('videoCreation', videoCreation, name='videoCreation'),
]

