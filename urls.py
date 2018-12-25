from django.conf.urls import url
from django.contrib import admin
from main import views
from . import views
from django.urls import path

urlpatterns = [
  path('', views.home),
  path('count/', views.count, name = "count"),
  
]
