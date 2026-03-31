from django.db import models

# ==========================================
# MODULE 1: Food Item Model (আগের কোড)
# ==========================================
class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==========================================
# MODULE 2: Order Models (নতুন কোড)
# ==========================================
class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True, blank=True)
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status_choices = (
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id} - {self.student_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.food_item.name} for {self.order.order_id}"