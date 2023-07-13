from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
]
