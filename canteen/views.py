"""
View Functions
Module 1: Display and filter food items
"""
from django.shortcuts import render, get_object_or_404
from .models import FoodItem, Category


def home(request):
    """
    Homepage with food items and category filtering
    Suman: FR-1 - Display items
    Emamul: FR-2 - Category filtering
    Arin: FR-3 - Availability status
    """
    # Emamul's Part - Get selected category from URL
    selected_category = request.GET.get('category', 'all')
    
    # Get all categories for filter buttons
    categories = Category.objects.all()
    
    # Filter food items
    if selected_category == 'all':
        food_items = FoodItem.objects.filter(is_available=True)
    else:
        food_items = FoodItem.objects.filter(
            category__name=selected_category,
            is_available=True
        )
    
    context = {
        'food_items': food_items,
        'categories': categories,
        'selected_category': selected_category,
    }
    
    return render(request, 'canteen/home.html', context)


def menu_view(request):
    """
    Full menu page with items grouped by category
    Emamul's Part - Category organization
    """
    categories = Category.objects.all()
    menu_data = []
    
    for category in categories:
        items = FoodItem.objects.filter(category=category, is_available=True)
        if items.exists():
            menu_data.append({
                'category': category,
                'items': items
            })
    
    context = {
        'menu_data': menu_data,
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
    }
    
    return render(request, 'canteen/food_detail.html', context)