from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.store.models.category import Category
from ecommerce.store.models.product import Product
from ecommerce.store.models.subcategory import Subcategory

User = get_user_model()


class ProductUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Eletrônicos')
        cls.subcategory = Subcategory.objects.create(
            name='Smartphones', category=cls.category
        )
        cls.product = Product.objects.create(
            brand='Samsung',
            name='Samsung Galaxy A10',
            description='X',
            price=699.00,
            quantity=100,
            subcategory=cls.subcategory,
        )

    def test_format_str_magic_method(self):
        expected = f'{self.product.brand} - {self.product.name}'

        self.assertEqual(str(self.product), expected)
