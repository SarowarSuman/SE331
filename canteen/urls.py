from django.urls import path
from . import views

app_name = 'canteen'

urlpatterns = [
    # Module 1 routes (আপনার এররটি হচ্ছিল কারণ এগুলো ডিলিট হয়ে গিয়েছিল)
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    
    # Module 2 routes
    path('place-order/', views.place_order, name='place_order'),
    path('order-success/<str:order_id>/', views.order_success, name='order_success'),
]