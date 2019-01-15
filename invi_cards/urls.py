from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
    path('E_Form/', Forms, name="E_Form")

]
