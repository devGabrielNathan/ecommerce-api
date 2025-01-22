from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.orders.models.order_item import OrderItem
from ecommerce.store.models.category import Category
from ecommerce.store.models.product import Product
from ecommerce.store.models.subcategory import Subcategory

User = get_user_model()


class OrderUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Eletrônicos')
        cls.subcategory = Subcategory.objects.create(
            name='Celulares', category=cls.category
        )
        cls.product = Product.objects.create(
            brand='Samsung',
            name='Samsung Galaxy A10',
            description='X',
            price=699.00,
            quantity=100,
            subcategory=cls.subcategory,
        )
        cls.user = User.objects.create_user(
            username='UserTest', email='teste@gmail.com', password='123456789'
        )
        cls.order = OrderItem.objects.create(user=cls.user)

        cls.order_item = OrderItem.objects.create(
            order=cls.order, product=cls.product
        )

    def test_str_magic_method(self):
        expected = f'{self.product.name} ({self.order_item.quantity})'

        self.assertEqual(str(self.order_item), expected)
