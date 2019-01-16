from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
<<<<<<< HEAD
    path('E_Form/', Forms, name="E_Form"),
	path('draw', on_draw, name='draw' )
=======
	path('draw', on_draw, name='draw' ),
	path('reset', reset, name='reset')

>>>>>>> cd0e2f6d1434a0d90f3cbab716bf8fb6ddd64331
]
