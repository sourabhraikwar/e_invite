from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('reset', reset, name='reset'),
	path('signup', signup, name='signup'),
]
