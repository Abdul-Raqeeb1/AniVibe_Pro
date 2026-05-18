from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('fetch-data/', views.fetch_trending_data, name='fetch_data'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),
    path('show/<int:id>/', views.show_detail, name='show_detail'),
]
