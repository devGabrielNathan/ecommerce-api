from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.store.models.category import Category

User = get_user_model()


class CategoryUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Eletrônicos')

    def test_format_str_magic_method(self):
        expected = f'{self.category.name}'

        self.assertEqual(str(self.category), expected)
