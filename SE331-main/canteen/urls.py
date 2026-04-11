"""
URL patterns for canteen app
"""
from django.urls import path
from . import views

app_name = 'canteen'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('item/<int:item_id>/', views.food_item_detail, name='food_detail'),
]