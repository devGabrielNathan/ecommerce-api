from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ecommerce.store.models.product import Product

User = get_user_model()

class CommonSetUp(APITestCase):
    fixtures = ['categories.json', 'subcategories.json', 'products.json']

    def setUp(self):
        self.product_id = Product.objects.get(
            pk='905a69f3-11db-4f99-b80f-23d5ba2be758'
        )
        self.invalid_product_id = 'ceead403-f0e9-40c0-ac6a-6f33c7f39c25'

        self.url = reverse('product-list')
        self.invalid_url = 'invalid-url/'

        self.url_with_id = reverse(
            'product-detail', kwargs={'pk': str(self.product_id.id)}
        )
        self.invalid_url_with_id = f'products/{str(self.invalid_product_id)}/'

class ProductListIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()

    def test_get_all_products_and_return_status_200_ok(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class productDetailIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()

    def test_get_product_by_id_and_return_status_200_ok(self):
        response = self.client.get(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_by_id_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
