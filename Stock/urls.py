from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('Stock/',views.Stock),
    
]