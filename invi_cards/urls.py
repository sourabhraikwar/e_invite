from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
    path('E_Form/', Forms, name="E_Form"),
	path('draw', on_draw, name='draw' ),
	path('reset', reset, name='reset'),
	path('signup', signup, name='signup'),
	path('profile', profile, name='profile'),


]
