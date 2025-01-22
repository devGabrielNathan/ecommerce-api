from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.store.models.category import Category
from ecommerce.store.models.subcategory import Subcategory

User = get_user_model()


class SubcategoryUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Eletrônicos')
        cls.Subcategory = Subcategory.objects.create(
            name='Celulares', category=cls.category
        )

    def test_format_str_magic_method(self):
        expected = f'{self.Subcategory.name}'

        self.assertEqual(str(self.Subcategory), expected)
