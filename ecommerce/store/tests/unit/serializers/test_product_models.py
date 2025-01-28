from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.store.models.product import Product
from ecommerce.store.models.category import Category
from ecommerce.store.models.subcategory import Subcategory
from uuid import uuid4

from ecommerce.store.serializers.product import ProductListSerializer, ProductDetailSerializer

User = get_user_model()

class CommonSetUp(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category_attributes = {
            'id': uuid4(),
            'name': 'Eletrônicos',
            'status': 'active',
        }
        cls.category = Category.objects.create(**cls.category_attributes)

        cls.subcategory_attributes = {
            'id': uuid4(),
            'name': 'Smartphones',
            'status': 'active',
            'category': cls.category
        }
        cls.subcategory = Subcategory.objects.create(**cls.subcategory_attributes)

        cls.product_attributes = {
            'id': uuid4(),
            'brand': 'Apple',
            'name': 'iPhone 12',
            'description': 'iPhone 12 64GB',
            'price': '7999.99',
            'quantity': 10,
            'status': 'active',
            'subcategory': cls.subcategory
        }

        cls.product = Product.objects.create(**cls.product_attributes)

class ProductListSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = ProductListSerializer(instance=self.product)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            [
                'id',
                'brand',
                'name',
                'description',
                'price',
                'quantity',
                'status',
                'subcategory'
            ],
        )

    def test_brand_field_content(self):
        self.assertEqual(self.data['brand'], self.product_attributes['brand'])

    def test_name_field_content(self):
        self.assertEqual(self.data['name'], self.product_attributes['name'])

    def test_description_field_content(self):
        self.assertEqual(self.data['description'], self.product_attributes['description'])

    def test_price_field_content(self):
        self.assertEqual(self.data['price'], self.product_attributes['price'])

    def test_quantity_field_content(self):
        self.assertEqual(self.data['quantity'], self.product_attributes['quantity'])

    def test_status_field_content(self):
        self.assertEqual(self.data['status'], self.product_attributes['status'])

    def test_subcategory_field_content(self):
        self.assertEqual(self.data['subcategory'], self.product_attributes['subcategory'].id)


class ProductDetailSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = ProductDetailSerializer(instance=self.product)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            [
                'id',
                'brand',
                'name',
                'description',
                'price',
                'quantity',
                'status',
                'subcategory'
            ],
        )

    def test_brand_field_content(self):
        self.assertEqual(self.data['brand'], self.product_attributes['brand'])

    def test_name_field_content(self):
        self.assertEqual(self.data['name'], self.product_attributes['name'])

    def test_description_field_content(self):
        self.assertEqual(self.data['description'], self.product_attributes['description'])

    def test_price_field_content(self):
        self.assertEqual(self.data['price'], self.product_attributes['price'])

    def test_quantity_field_content(self):
        self.assertEqual(self.data['quantity'], self.product_attributes['quantity'])

    def test_status_field_content(self):
        self.assertEqual(self.data['status'], self.product_attributes['status'])

    def test_subcategory_field_content(self):
        self.assertEqual(self.data['subcategory'], self.product_attributes['subcategory'].id)