from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
    path('E_Form/', Forms, name="E_Form"),
	path('reset', reset, name='reset'),
	path('signup', signup, name='signup'),
	path('profile', profile, name='profile'),
	path('my',my_profile,),
	path('card', card, name='card' ),
]
