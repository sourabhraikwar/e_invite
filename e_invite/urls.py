from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('invi_cards.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# this is a comment