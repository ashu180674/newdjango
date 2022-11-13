from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
   
   path('', views.index , name='home'),
   path('aboutus', views.aboutus, name="about"),
   path('services', views.services, name="services"),
   path('contactus', views.contactus, name="contactus"),
   path('icecream', views.icecream, name="icecream")
   
]
 