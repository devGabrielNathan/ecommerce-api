from uuid import uuid4

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.store.models.category import Category
from ecommerce.store.models.subcategory import Subcategory
from ecommerce.store.serializers.subcategory import (
    SubcategoryDetailSerializer,
    SubcategoryListSerializer,
)

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
            'category': cls.category,
        }
        cls.subcategory = Subcategory.objects.create(
            **cls.subcategory_attributes
        )


class SubcategoryListSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = SubcategoryListSerializer(instance=cls.subcategory)
        cls.data = cls.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            ['id', 'name', 'status', 'category'],
        )

    def test_name_field_content(self):
        self.assertEqual(
            self.data['name'], self.subcategory_attributes['name']
        )

    def test_status_field_content(self):
        self.assertEqual(
            self.data['status'], self.subcategory_attributes['status']
        )

    def test_category_field_content(self):
        self.assertEqual(
            self.data['category'], self.subcategory_attributes['category'].id
        )


class SubcategoryDetailSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = SubcategoryDetailSerializer(instance=cls.subcategory)
        cls.data = cls.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            ['id', 'name', 'status', 'category'],
        )

    def test_name_field_content(self):
        self.assertEqual(
            self.data['name'], self.subcategory_attributes['name']
        )

    def test_status_field_content(self):
        self.assertEqual(
            self.data['status'], self.subcategory_attributes['status']
        )

    def test_category_field_content(self):
        self.assertEqual(
            self.data['category'], self.subcategory_attributes['category'].id
        )
