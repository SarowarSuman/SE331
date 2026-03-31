from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .models import FoodItem, Order, OrderItem
import datetime

# ==========================================
# MODULE 1: VIEWS (আগের কোড)
# ==========================================
def home(request):
    # হোম পেইজে দেখানোর জন্য ৩টি এভেইলেবল আইটেম
    featured_items = FoodItem.objects.filter(is_available=True)[:3]
    return render(request, 'canteen/home.html', {'featured_items': featured_items})

def menu_view(request):
    # মেনু পেইজের জন্য সব এভেইলেবল আইটেম
    food_items = FoodItem.objects.filter(is_available=True)
    return render(request, 'canteen/menu.html', {'food_items': food_items})

def food_item_detail(request, item_id):
    # ফুড ডিটেইলস পেইজ
    item = get_object_or_404(FoodItem, id=item_id)
    return render(request, 'canteen/food_detail.html', {'item': item})


# ==========================================
# MODULE 2: VIEWS (নতুন কোড)
# ==========================================
def place_order(request):
    food_items = FoodItem.objects.filter(is_available=True)
    
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        phone = request.POST.get('phone')
        
        # জেনারেট Order ID (e.g., ORD-20231025123045)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        order_id = f"ORD-{timestamp}"
        
        try:
            with transaction.atomic():
                # নতুন অর্ডার তৈরি
                order = Order.objects.create(
                    order_id=order_id,
                    student_name=student_name,
                    student_id=student_id,
                    phone=phone
                )
                
                total_amount = 0
                
                # নির্বাচিত আইটেমগুলো চেক করা
                for item in food_items:
                    checkbox_name = f"item_{item.id}"
                    if request.POST.get(checkbox_name):
                        qty = int(request.POST.get(f"qty_{item.id}", 1))
                        price = item.price * qty
                        total_amount += price
                        
                        # অর্ডার আইটেম সেভ করা
                        OrderItem.objects.create(
                            order=order,
                            food_item=item,
                            quantity=qty,
                            price=item.price
                        )
                
                # যদি কোনো আইটেম সিলেক্ট না করে
                if total_amount == 0:
                    messages.error(request, "Please select at least one item!")
                    return redirect('canteen:place_order')
                    
                # টোটাল এমাউন্ট আপডেট করা
                order.total_amount = total_amount
                order.save()
                
                return redirect('canteen:order_success', order_id=order.order_id)
                
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('canteen:place_order')
            
    return render(request, 'canteen/place_order.html', {'food_items': food_items})

def order_success(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'canteen/order_success.html', {'order': order})