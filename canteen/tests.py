from django.test import TestCase
from django.urls import reverse

from .models import Category, FoodItem, Order


class MenuBrowsingTests(TestCase):
    def setUp(self):
        self.breakfast = Category.objects.create(name='breakfast', description='Morning food')
        self.drinks = Category.objects.create(name='drinks', description='Beverages')

        FoodItem.objects.create(
            category=self.breakfast,
            name='Paratha Combo',
            description='Paratha with egg',
            price='60.00',
            is_available=True,
        )
        FoodItem.objects.create(
            category=self.breakfast,
            name='Toast',
            description='Butter toast',
            price='30.00',
            is_available=False,
        )
        FoodItem.objects.create(
            category=self.drinks,
            name='Lemon Juice',
            description='Fresh drink',
            price='45.00',
            is_available=True,
        )

    def test_home_filters_by_category(self):
        response = self.client.get(reverse('canteen:home'), {'category': 'drinks'})
        self.assertEqual(response.status_code, 200)
        items = response.context['food_items']
        self.assertEqual(items.count(), 1)
        self.assertEqual(items.first().name, 'Lemon Juice')

    def test_home_search_and_availability_filter(self):
        response = self.client.get(
            reverse('canteen:home'),
            {'q': 'toast', 'availability': 'all', 'category': 'all'}
        )
        self.assertEqual(response.status_code, 200)
        items = response.context['food_items']
        self.assertEqual(items.count(), 1)
        self.assertEqual(items.first().name, 'Toast')

    def test_menu_view_groups_available_items(self):
        response = self.client.get(reverse('canteen:menu'))
        self.assertEqual(response.status_code, 200)
        menu_data = response.context['menu_data']
        category_names = [entry['category'].name for entry in menu_data]
        self.assertIn('breakfast', category_names)
        self.assertIn('drinks', category_names)

        breakfast_items = next(entry['items'] for entry in menu_data if entry['category'].name == 'breakfast')
        self.assertEqual(breakfast_items.count(), 1)
        self.assertEqual(breakfast_items.first().name, 'Paratha Combo')


class OrderPlacementTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='lunch', description='Lunch items')
        self.food_item = FoodItem.objects.create(
            category=self.category,
            name='Chicken Rice',
            description='Rice with chicken curry',
            price='120.00',
            is_available=True,
        )

    def test_place_order_with_valid_student_info(self):
        response = self.client.post(
            reverse('canteen:place_order', args=[self.food_item.id]),
            {
                'student_name': 'Arin Hasan',
                'student_id': '2023-1-60-123',
                'phone_number': '01712345678',
                'quantity': 2,
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'canteen/order_success.html')
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.first().quantity, 2)

    def test_place_order_requires_all_fields(self):
        response = self.client.post(
            reverse('canteen:place_order', args=[self.food_item.id]),
            {
                'student_name': '',
                'student_id': '',
                'phone_number': '',
                'quantity': 0,
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'canteen/food_detail.html')
        self.assertEqual(Order.objects.count(), 0)
        form = response.context['order_form']
        self.assertIn('student_name', form.errors)
        self.assertIn('student_id', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('quantity', form.errors)


class OrderTrackingAndHistoryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='snacks', description='Snacks items')
        self.food_item = FoodItem.objects.create(
            category=self.category,
            name='Chicken Roll',
            description='Hot roll',
            price='80.00',
            is_available=True,
        )
        self.order = Order.objects.create(
            food_item=self.food_item,
            quantity=3,
            student_name='Arin Hasan',
            student_id='2023-1-60-123',
            phone_number='01712345678',
            status=Order.STATUS_PREPARING,
        )

    def test_track_order_by_id(self):
        response = self.client.get(
            reverse('canteen:track_order'),
            {'track-order': '1', 'track-order_id': self.order.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['tracked_order'].id, self.order.id)

    def test_order_history_shows_breakdown(self):
        response = self.client.get(
            reverse('canteen:track_order'),
            {
                'history-lookup': '1',
                'history-student_id': '2023-1-60-123',
                'history-phone_number': '01712345678'
            }
        )
        self.assertEqual(response.status_code, 200)
        history_orders = response.context['history_orders']
        self.assertEqual(history_orders.count(), 1)
        history_order = history_orders.first()
        self.assertEqual(history_order.food_item.name, 'Chicken Roll')
        self.assertEqual(history_order.quantity, 3)
