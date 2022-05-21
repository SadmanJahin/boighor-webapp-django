from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.viewallBook,name='allBook'),
path('education/', views.viewBookCategoryEducation,name='education'),
path('sci-fi/', views.viewBookCategoryScifi,name='sci-fi'),
path('search/', views.viewSearchedBooks,name='search'),
    
    
]
