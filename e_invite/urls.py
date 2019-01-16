"""e_invite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
import django.contrib.auth
=======
import django.contrib.auth 

>>>>>>> cd0e2f6d1434a0d90f3cbab716bf8fb6ddd64331

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('invi_cards.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
=======

>>>>>>> cd0e2f6d1434a0d90f3cbab716bf8fb6ddd64331
]
