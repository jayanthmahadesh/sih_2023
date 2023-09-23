from django.contrib import admin
from django.urls import path
from myapp import views
from .views import case_file,signup,judge_dash,login,dashboard
urlpatterns = [
    path('',views.landing,name='landing'),
    path('dashboard',dashboard.as_view(),name='dashboard'),
    path('case_file',case_file.as_view(),name='case_file'),
    path('signup',signup.as_view(),name='signup'),
    path('judge_dash',judge_dash.as_view(),name='judge_dash'),
    path('verify_otp',views.send_otp_email,name='verify'),
    path('login',login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('otp',views.send_otp_email,name='otp')
]
