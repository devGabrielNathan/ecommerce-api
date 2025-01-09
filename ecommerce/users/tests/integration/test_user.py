from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import copy

User = get_user_model()


class UserIntegrationTest(APITestCase):
    def setUp(self) -> None:
        self.payload = {
            'username': 'test',
            'email': 'teste@gmail.com',
            'password': '123456789',
            'password_confirmation': '123456789'
            }
        self.invalid_payload = {
            'username': 'test',
            'email': 'teste@gmail.com',
            'password': '123456789',
            }

        self.url = reverse('user-list')

    def test_create_user_and_return_status_code_201_created(self):
        response = self.client.post(self.url, self.payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_user_and_return_status_code_400_bad_request(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password_confirmation'][0].title(), 'Este Campo É Obrigatório.')

    def test_create_superuser_and_return_status_code_201_created(self):
        new_payload = copy.deepcopy(self.payload)
        new_payload['is_superuser'] = True

        response = self.client.post(self.url, new_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_superuser_and_return_status_code_400_bad_request(self):
        new_payload = copy.deepcopy(self.invalid_payload)
        new_payload['is_superuser'] = True

        response = self.client.post(self.url, new_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password_confirmation'][0].title(), 'Este Campo É Obrigatório.')

        # self.user = User.objects.create(
        #     username='UserTest',
        #     email='teste@gmail.com',
        #     password='123456789'
        #     )
        # self.super_user = User.objects.create(
        #     username='UserTest',
        #     email='teste@gmail.com',
        #     password='123456789',
        #     is_superuser = True
        #     )
