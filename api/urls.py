from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('search_results/', views.search_results, name='search_results'),
    path('discover/', views.discover, name='discover'),
    path('watchlist/add/<int:id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('delete_watchlist/', views.delete_watchlist, name='delete_watchlist'),
    ]
