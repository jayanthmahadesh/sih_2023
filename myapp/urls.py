from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('dashboard',views.dashboard,name='dashboard'),
]
