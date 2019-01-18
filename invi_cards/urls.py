from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
    path('E_Form/', Forms, name="E_Form"),
	path('draw', on_draw, name='draw' ),
	path('fire', fire, name='fire' ),
	path('scrap', browser_scrap, name='scrap' ),
]
