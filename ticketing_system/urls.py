from django.contrib import admin
from django.urls import path, include
from tickets.api import api  # pridaj

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tickets.urls')),
    path('api/', api.urls),  # pridaj toto
]