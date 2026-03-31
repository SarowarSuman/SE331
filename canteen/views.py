"""
View Functions
Module 1: Display and filter food items
"""
from django.shortcuts import render, get_object_or_404
from .models import FoodItem, Category, Order
from .forms import OrderPlacementForm, OrderTrackingForm, OrderHistoryLookupForm


def home(request):
    """
    Homepage with food items and category filtering
    Suman: FR-1 - Display items
    Emamul: FR-2 - Category filtering
    Arin: FR-3 - Availability status
    """
    # Emamul's Part - Get selected category from URL
    selected_category = request.GET.get('category', 'all')
    query = request.GET.get('q', '').strip()
    availability = request.GET.get('availability', 'available')
    
    # Get all categories for filter buttons
    categories = Category.objects.all()
    
    # Start with all food items and apply filters step by step.
    food_items = FoodItem.objects.select_related('category').all()

    if selected_category != 'all':
        food_items = food_items.filter(category__name=selected_category)

    if availability == 'available':
        food_items = food_items.filter(is_available=True)
    elif availability == 'sold_out':
        food_items = food_items.filter(is_available=False)

    if query:
        food_items = food_items.filter(name__icontains=query)
    
    context = {
        'food_items': food_items,
        'categories': categories,
        'selected_category': selected_category,
        'query': query,
        'availability': availability,
    }
    
    return render(request, 'canteen/home.html', context)


def menu_view(request):
    """
    Full menu page with items grouped by category
    Emamul's Part - Category organization
    """
    selected_category = request.GET.get('category', 'all')
    query = request.GET.get('q', '').strip()

    categories = Category.objects.all()
    base_items = FoodItem.objects.select_related('category').filter(is_available=True)
    if query:
        base_items = base_items.filter(name__icontains=query)

    if selected_category != 'all':
        categories = categories.filter(name=selected_category)

    menu_data = []
    
    for category in categories:
        items = base_items.filter(category=category)
        if items.exists():
            menu_data.append({
                'category': category,
                'items': items
            })
    
    context = {
        'menu_data': menu_data,
        'categories': Category.objects.all(),
        'selected_category': selected_category,
        'query': query,
    }
    
    return render(request, 'canteen/menu.html', context)


def food_item_detail(request, item_id):
    """
    Detailed view of a single food item
    All team members' features combined
    """
    food_item = get_object_or_404(FoodItem, id=item_id)
    
    # Get related items from same category
    related_items = FoodItem.objects.filter(
        category=food_item.category,
        is_available=True
    ).exclude(id=item_id)[:4]
    
    context = {
        'food_item': food_item,
        'related_items': related_items,
        'order_form': OrderPlacementForm(),
    }
    
    return render(request, 'canteen/food_detail.html', context)


def place_order(request, item_id):
    """
    Module 2: Collect and validate student information during order placement.
    """
    food_item = get_object_or_404(FoodItem, id=item_id, is_available=True)
    form = OrderPlacementForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        order = form.save(commit=False)
        order.food_item = food_item
        order.save()
        return render(request, 'canteen/order_success.html', {'order': order})

    related_items = FoodItem.objects.filter(
        category=food_item.category,
        is_available=True
    ).exclude(id=item_id)[:4]

    context = {
        'food_item': food_item,
        'related_items': related_items,
        'order_form': form,
    }
    return render(request, 'canteen/food_detail.html', context)


def track_order(request):
    """
    Module 3: Track order status by Order ID and view history.
    """
    tracking_form = OrderTrackingForm(request.GET or None, prefix='track')
    history_form = OrderHistoryLookupForm(request.GET or None, prefix='history')
    tracked_order = None
    tracking_not_found = False
    history_orders = None

    if 'track-order' in request.GET and tracking_form.is_valid():
        tracked_order = Order.objects.select_related('food_item').filter(id=tracking_form.cleaned_data['order_id']).first()
        tracking_not_found = tracked_order is None

    if 'history-lookup' in request.GET and history_form.is_valid():
        history_orders = Order.objects.select_related('food_item').filter(
            student_id=history_form.cleaned_data['student_id'].strip(),
            phone_number=history_form.cleaned_data['phone_number'].strip(),
        )

    context = {
        'tracking_form': tracking_form,
        'history_form': history_form,
        'tracked_order': tracked_order,
        'tracking_not_found': tracking_not_found,
        'history_orders': history_orders,
    }
    return render(request, 'canteen/order_tracking.html', context)