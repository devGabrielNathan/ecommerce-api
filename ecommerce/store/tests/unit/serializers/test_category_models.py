from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.store.models.category import Category
from uuid import uuid4

from ecommerce.store.serializers.category import CategoryListSerializer
from ecommerce.store.serializers.category import CategoryDetailSerializer

User = get_user_model()

class CommonSetUp(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.category_attributes = {
            'id': uuid4(),
            'name': 'Eletrônicos',
            'status': 'active',
        }
        self.category = Category.objects.create(**self.category_attributes)

class CategoryListSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = CategoryListSerializer(instance=self.category)
    def test_format_str_magic_method(self):
        expected = f'{self.category.name}'

        self.assertEqual(str(self.category), expected)

class CategoryDetailSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = CategoryDetailSerializer(instance=self.category)
        self.data = self.serializer.data
    
    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            [
                'id',
                'name',
                'status'
            ],
        )

    def test_name_field_content(self):
        self.assertEqual(self.data['name'], self.category_attributes['name'])

    def test_status_field_content(self):
        self.assertEqual(self.data['status'], self.category_attributes['status'])
