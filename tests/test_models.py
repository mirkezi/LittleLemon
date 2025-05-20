from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="Icecream", price=3.49, inventory= 10)
        itemstr = str(item)
        self.assertEqual(itemstr, "Icecream : 3.49")
