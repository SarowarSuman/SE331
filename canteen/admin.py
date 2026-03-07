"""
Admin Panel Configuration
Module 1: Food Menu Management
"""
from django.contrib import admin
from .models import Category, FoodItem


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

# Customize Admin Site
from django.contrib import admin

admin.site.site_header = "Administration"
admin.site.site_title = "Campus Canteen Admin"
admin.site.index_title = "Welcome to Campus Food Pre-Order System"    