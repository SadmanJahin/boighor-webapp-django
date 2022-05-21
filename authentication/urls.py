from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('registration/', views.registration,name='registration'),
    path('logout/', views.userlogout, name='logout'),
]
