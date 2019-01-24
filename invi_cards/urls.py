from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('aboutus', aboutUs, name='aboutus'),
	path('contactus', contactUs, name='contactus'),
	path('reset', reset, name='reset'),
	path('signup', signup, name='signup'),
	path('card', card, name='card' ),
]
