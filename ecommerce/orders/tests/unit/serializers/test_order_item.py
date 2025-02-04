from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.orders.models.order import Order
from ecommerce.orders.models.order_item import OrderItem
from ecommerce.orders.serializers.order_item import OrderItemSerializer
from ecommerce.store.models.category import Category
from ecommerce.store.models.product import Product
from ecommerce.store.models.subcategory import Subcategory

User = get_user_model()


class OrderItemSerializerUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls_user_attributes = {
            'username': 'Testando',
            'email': 'testando@testando.com',
            'password': 'testando@testando123',
            'password_confirmation': 'testando@teste123',
        }
        cls.user = User.objects.create_user(
            username=cls_user_attributes['username'],
            email=cls_user_attributes['email'],
            password=cls_user_attributes['password'],
        )
        cls.category = Category.objects.create(name='Eletrônicos')
        cls.subcategory = Subcategory.objects.create(
            name='Celulares', category=cls.category
        )
        cls.product_attributes = {
            'brand': 'Samsung',
            'name': 'Samsung Galaxy A10',
            'description': 'X',
            'price': 699.00,
            'quantity': 2,
            'subcategory': cls.subcategory,
        }
        cls.product = Product.objects.create(**cls.product_attributes)
        cls_order = Order.objects.create(user=cls.user)

        cls.order_item = OrderItem.objects.create(
            order=cls_order, product=cls.product, quantity=1
        )
        serializer = OrderItemSerializer(instance=cls.order_item)
        cls.data = serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(), ['id', 'product', 'quantity', 'subtotal']
        )

    def test_product_field_content(self):
        self.assertEqual(self.data['product'], self.order_item.product.id)

    def test_quantity_field_content(self):
        self.assertEqual(self.data['quantity'], self.order_item.quantity)

    def test_subtotal_field_content(self):
        self.assertEqual(
            self.data['subtotal'], f'{self.order_item.subtotal:.2f}'
        )
