from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
	path('somedata/', newpage, name='login' )
]
