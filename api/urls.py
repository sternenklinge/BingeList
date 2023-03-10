from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('results/', views.results, name='results'),
    path('search/', views.search, name='search'),
    path('watchlist/add/<int:id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('delete_watchlist/', views.delete_watchlist, name='delete_watchlist'),
    ]
