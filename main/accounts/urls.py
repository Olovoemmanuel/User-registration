from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register', REGISTER, name='register'),
    path('', REGISTER, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('home', HOME, name= 'home'),
    path("password_reset", password_reset_request, name="password_reset")
]
