from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ecommerce.store.models.subcategory import Subcategory

User = get_user_model()


class CommonSetUp(APITestCase):
    fixtures = ['categories.json', 'subcategories.json']

    def setUp(self):
        self.subcategory_id = Subcategory.objects.get(
            pk='4d825b96-ef23-4218-b382-c4eb3618b0f0'
        )
        self.invalid_subcategory_id = '91bc564d-0401-4822-a9cd-7534034e1955'

        self.url = reverse('subcategory-list')
        self.invalid_url = 'invalid-url/'

        self.url_with_id = reverse(
            'subcategory-detail', kwargs={'pk': str(self.subcategory_id.id)}
        )
        self.invalid_url_with_id = (
            f'subcategories/{str(self.invalid_subcategory_id)}/'
        )


class ProductListIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()

    def test_get_all_subcategories_and_return_status_200_ok(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_subcategories_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SubCategoryDetailIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()

    def test_get_subcategory_by_id_and_return_status_200_ok(self):
        response = self.client.get(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_subcategory_by_id_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
