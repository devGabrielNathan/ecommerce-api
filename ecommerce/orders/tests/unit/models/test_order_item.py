from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.orders.models.order import Order
from ecommerce.orders.models.order_item import OrderItem
from ecommerce.store.models.category import Category
from ecommerce.store.models.product import Product
from ecommerce.store.models.subcategory import Subcategory

User = get_user_model()


class OrderItemUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='UserTest', email='teste@gmail.com', password='123456789'
        )
        cls.category = Category.objects.create(name='Eletrônicos')
        cls.subcategory = Subcategory.objects.create(
            name='Celulares', category=cls.category
        )
        cls.product = Product.objects.create(
            brand='Samsung',
            name='Samsung Galaxy A10',
            description='X',
            price=699.00,
            quantity=2,
            subcategory=cls.subcategory,
        )
        cls.order = Order.objects.create(user=cls.user)
        cls.order_item = OrderItem.objects.create(
            order=cls.order,
            product=cls.product,
        )

    def test_str_magic_method(self):
        expected = f'{self.product.name} ({self.order_item.quantity} - R$ {self.order_item.subtotal})'

        self.assertEqual(str(self.order_item), expected)

    def test_save_method(self):
        # print(self.order_item.quantity)
        # print(self.product.quantity)
        # print(self.order_item.subtotal)
        self.assertEqual(self.order_item.quantity, 2)
        self.assertEqual(self.product.quantity, 0)
        self.assertEqual(self.order_item.subtotal, 1398.00)
        self.order_item.save()
        # print(self.order_item.quantity)
        # print(self.product.quantity)
        # print(self.order_item.subtotal)
