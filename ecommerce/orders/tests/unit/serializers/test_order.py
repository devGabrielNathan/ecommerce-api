from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.orders.models.order import Order
from ecommerce.orders.models.order_item import OrderItem
from ecommerce.orders.serializers.order import (
    OrderDetailSerializer,
    OrderListCreateSerializer,
)
from ecommerce.store.models.category import Category
from ecommerce.store.models.product import Product
from ecommerce.store.models.subcategory import Subcategory

User = get_user_model()


class CommonSetUp(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_attributes = {
            'username': 'Testando',
            'email': 'testando@testando.com',
            'password': 'testando@testando123',
        }
        cls.user = User.objects.create_user(
            username=cls.user_attributes['username'],
            email=cls.user_attributes['email'],
            password=cls.user_attributes['password'],
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
        cls.order_attributes = {
            'user': cls.user,
            'items': [
                {
                    'product': cls.product,
                    'quantity': 2,
                }
            ],
        }
        cls.order_attributes.pop('items')
        cls.order = Order.objects.create(**cls.order_attributes)
        cls.order_item = OrderItem.objects.create(
            order=cls.order, product=cls.product, quantity=2
        )
        cls.order_with_items = {
            'id': str(cls.order.id),
            'user': str(cls.order.id),
            'items': [
                {
                    'product': cls.order_item.product.id,
                    'quantity': cls.order_item.quantity,
                    'subtotal': cls.order_item.subtotal,
                }
            ],
        }


class OrderListCreateSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.serializer = OrderListCreateSerializer(instance=cls.order)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'user', 'items'])

    def test_user_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['user'], self.order.user.id)

    def test_items_field_content(self):
        data = self.serializer.data
        self.assertEqual(len(data['items']), 1)
        self.assertEqual(
            data['items'][0]['product'], self.order_item.product.id
        )

    def test_create_order(self):
        payload = {
            'user': self.user.id,
            'items': [
                {
                    'product': self.product.id,
                    'quantity': 2,
                }
            ],
        }
        serializer = OrderListCreateSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        serializer.save()


class OrderDetailSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.serializer = OrderDetailSerializer(instance=cls.order)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'user', 'items'])

    def test_id_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['id'], str(self.order.id))

    def test_user_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['user'], self.order.user.id)

    def test_items_field_content(self):
        data = self.serializer.data
        self.assertEqual(len(data['items']), 1)
        self.assertEqual(
            data['items'][0]['product'], self.order_item.product.id
        )
