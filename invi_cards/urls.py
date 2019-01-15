from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
	path('draw', on_draw, name='draw' ),
	path('reset', reset, name='reset')

]
