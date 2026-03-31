from django.contrib import admin
from .models import FoodItem, Order, OrderItem

# ==========================================
# MODULE 1: Food Item Admin (আগের কোড)
# ==========================================
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at')
    list_filter = ('is_available',)
    search_fields = ('name',)

# ==========================================
# MODULE 2: Order Admin (নতুন কোড)
# ==========================================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'student_name', 'student_id', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'student_name', 'student_id')
    inlines = [OrderItemInline]