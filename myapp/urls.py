from django.contrib import admin
from django.urls import path
from myapp import views
from .views import case_file,signup
urlpatterns = [
    path('',views.landing,name='landing'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('case_file',case_file.as_view(),name='case_file'),
    path('signup',signup.as_view(),name='signup'),
]
