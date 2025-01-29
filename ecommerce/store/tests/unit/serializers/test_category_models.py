from uuid import uuid4

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.store.models.category import Category
from ecommerce.store.serializers.category import (
    CategoryDetailSerializer,
    CategoryListSerializer,
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


class CategoryListSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = CategoryListSerializer(instance=cls.category)
        cls.data = cls.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            ['id', 'name', 'status'],
        )

    def test_name_field_content(self):
        self.assertEqual(self.data['name'], self.category_attributes['name'])

    def test_status_field_content(self):
        self.assertEqual(
            self.data['status'], self.category_attributes['status']
        )


class CategoryDetailSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = CategoryDetailSerializer(instance=cls.category)
        cls.data = cls.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            ['id', 'name', 'status'],
        )

    def test_name_field_content(self):
        self.assertEqual(self.data['name'], self.category_attributes['name'])

    def test_status_field_content(self):
        self.assertEqual(
            self.data['status'], self.category_attributes['status']
        )
