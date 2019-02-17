"""
This module contain urls of invi_card modules.

Imported methods
----------------

these method imported from invi_cards.views module.

* home
* reset
* signup

"""
from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('reset', reset, name='reset'),
	path('signup', signup, name='signup'),
]
