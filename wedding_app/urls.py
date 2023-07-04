from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('venues', views.gallery, name = 'venues'),
    path('venue/<int:id>', views.venue, name = 'venue'),
    path('events', views.events, name = 'events'),
    path('AddVenue', views.AddVenue, name = 'AddVenue'),
    path('contact', views.contact, name = 'contact'),
]