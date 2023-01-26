from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('search_results/', views.search_results, name='search_results'),
    path('add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    ]
