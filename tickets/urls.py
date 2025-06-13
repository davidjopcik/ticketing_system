from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from tickets.api import api 

urlpatterns = [
    path('passengers/', views.passenger_list, name='passenger_list'),
    path('passenger/<int:passenger_id>/', views.passenger_detail, name='passenger_detail'),
    path('passenger/add/', views.passenger_create, name='passenger_create'),  
    path('ticket/sale/', views.ticket_sale_view, name='ticket_sale'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('stations/', views.station_list, name='station_list'),
    path('stations/create/', views.create_station, name='create_station'),
    path('stations/edit/<int:station_id>/', views.edit_station, name='edit_station'),
    path('passengers/search/', views.search_passenger, name='search_passenger'),
    path('zones/create/', views.create_zone, name='create_zone'),
    path('', views.home, name='home'),
]