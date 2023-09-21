from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.landing,name='landing'),
    path('dashboard',views.dashboard,name='dashboard'),
]
