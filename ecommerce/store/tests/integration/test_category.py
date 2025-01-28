from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ecommerce.store.models.category import Category

User = get_user_model()

class CommonSetUp(APITestCase):
    fixtures = ['categories.json']

    def setUp(self):
        self.category_id = Category.objects.get(
            pk='8f091eaf-a582-437c-ad2b-f689a69cf401'
        )
        self.invalid_category_id = 'e4b52674-bfd9-4bb6-80cb-09248f1ee361'

        self.url = reverse('category-list')
        self.invalid_url = 'invalid-url/'

        self.url_with_id = reverse(
            'category-detail', kwargs={'pk': str(self.category_id.id)}
        )
        self.invalid_url_with_id = f'category/{str(self.invalid_category_id)}/'


class CategoryListIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()

    def test_get_all_categories_and_return_status_200_ok(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_categories_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CategoryDetailIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()


    def test_get_category_by_id_and_return_status_200_ok(self):
        response = self.client.get(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_by_id_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
