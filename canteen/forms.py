from django import forms
from django.core.exceptions import ValidationError

from .models import Order


class OrderPlacementForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['student_name', 'student_id', 'phone_number', 'quantity']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2024-1-60-001'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 01712345678'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
        }

    def clean_student_name(self):
        value = self.cleaned_data['student_name'].strip()
        if not value:
            raise ValidationError("Student name is required.")
        return value

    def clean_student_id(self):
        value = self.cleaned_data['student_id'].strip()
        if not value:
            raise ValidationError("Student ID is required.")
        return value

    def clean_phone_number(self):
        value = self.cleaned_data['phone_number'].strip()
        if not value:
            raise ValidationError("Phone number is required.")
        digits = ''.join(ch for ch in value if ch.isdigit())
        if len(digits) < 10:
            raise ValidationError("Enter a valid phone number.")
        return value

    def clean_quantity(self):
        value = self.cleaned_data['quantity']
        if value < 1:
            raise ValidationError("Quantity must be at least 1.")
        if value > 20:
            raise ValidationError("Quantity cannot exceed 20.")
        return value


class OrderTrackingForm(forms.Form):
    order_id = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your order ID'}
        )
    )


class OrderHistoryLookupForm(forms.Form):
    student_id = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your Student ID'}
        )
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}
        )
    )
