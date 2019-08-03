from django.test import TestCase
from .models import Product

# Create your tests here.

class ProductTest(TestCase):
    
    def test_str(self):
        
        test_name = Product(name='Test name')
        self.assertEqual(str(test_name),'Test name')