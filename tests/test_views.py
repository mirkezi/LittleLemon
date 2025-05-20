from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.urls import reverse

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=9.99, inventory=20)
        self.menu2 = Menu.objects.create(title="Pinsa", price=8.99, inventory=18)
        self.menu3 = Menu.objects.create(title="Pasta", price=7.99, inventory=30)
    
    def test_getall(self):
        
        response = self.client.get(reverse('menu-list'))
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        
        self.assertEqual(response.data, serialized_items.data)