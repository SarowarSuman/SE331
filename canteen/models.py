"""
Database Models for Campus Food Pre-Order System
Module 1: Food Menu Browsing and Categorization
"""
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    Category model for organizing food items
    FR-2: Categories (Breakfast, Lunch, Snacks, Drinks)
    Emamul's Feature
    """
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('snacks', 'Snacks'),
        ('drinks', 'Drinks'),
    ]
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.get_name_display()


class FoodItem(models.Model):
    """
    Food Item model storing menu items
    Suman's Features: FR-1 (Display items), FR-6 (Image handling)
    Arin's Feature: FR-3 (Availability status)
    """
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='food_items'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    
    # Arin's Part - FR-3: Availability tracking
    is_available = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'name']
    
    def __str__(self):
        return f"{self.name} - ৳{self.price}"
    
    def get_image_url(self):
        """
        Suman's Part - FR-6: Return image URL or placeholder
        """
        if self.image:
            return self.image.url
        else:
            return '/static/images/placeholder-food.png'
    
    def get_availability_status(self):
        """
        Arin's Part - FR-3: Get availability status display
        """
        return "Available" if self.is_available else "Sold Out"
    
    def get_availability_class(self):
        """
        CSS class for availability badge
        """
        return "bg-success" if self.is_available else "bg-danger"