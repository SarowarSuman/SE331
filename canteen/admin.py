"""
Admin Panel Configuration
Module 1: Food Menu Management
"""
from django.contrib import admin
from .models import Category, FoodItem, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin Panel
    """
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at']


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    """
    Food Item Admin Panel
    Suman: Image management
    Arin: Availability quick-edit
    """
    list_display = ['name', 'category', 'price', 'is_available', 'created_at']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_available', 'price']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'description')
        }),
        ('Pricing & Availability', {
            'fields': ('price', 'is_available')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Module 2 - Order management from admin panel.
    """
    list_display = ['id', 'food_item', 'quantity', 'student_name', 'student_id', 'phone_number', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'food_item__category']
    search_fields = ['student_name', 'student_id', 'phone_number', 'food_item__name']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Order Details', {
            'fields': ('food_item', 'quantity', 'status')
        }),
        ('Student Information', {
            'fields': ('student_name', 'student_id', 'phone_number')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Customize Admin Site

admin.site.site_header = "Administration"
admin.site.site_title = "Campus Canteen Admin"
admin.site.index_title = "Welcome to Campus Food Pre-Order System"    