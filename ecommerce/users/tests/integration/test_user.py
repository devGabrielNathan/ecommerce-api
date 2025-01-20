import copy

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class UserIntegrationTest(APITestCase):
    fixtures = ['users.json']

    def setUp(self) -> None:
        self.user_id = User.objects.get(pk='d19fb71e-7140-468b-899c-9b940da2476c')
        self.invalid_user_id = 'acb2aedb-94f9-4eec-ad83-f3c749a05b99'
        self.client = APIClient()
        self.client.force_authenticate(user=self.user_id)

        self.url = reverse('user-list')
        self.invalid_url = 'invalid-url/'

        self.url_with_id = reverse('user-detail', kwargs={'pk': str(self.user_id.id)})
        self.invalid_url_with_id = f'users/{str(self.invalid_user_id)}/'

        self.payload_patch = {
            'username': 'ADMIN',
            'email': 'teste@gmail.com'
        }
        self.payload_update_user_detail = {
            'username': 'teste',
            'email': 'teste@gmail.com'
        }
        self.invalid_payload_update_user_detail = {
            'username': 'teste'
        }
        self.payload_update_reset_password = {
            'old_password': self.user_id.password,
            'username': 'teste',
            'email': 'teste@gmail.com'
        }
        self.invalid_payload_update_reset_password = {
            'new_password': 'teste123',
            'password_confirmation': 'teste123'
        }
        self.payload_post = {
            'username': 'teste2',
            'email': 'teste2@gmail.com',
            'password': '123456789',
            'password_confirmation': '123456789',
        }
        self.invalid_payload_post = {
            'username': 'teste2',
            'email': 'teste@gmail.com',
            'password': '123456789',
        }

        self.url = reverse('user-list')

    def test_get_user_by_id_and_return_status_200_ok(self):
        response = self.client.get(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_user_by_id_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_user_by_id_and_return_status_204_no_content(self):
        response = self.client.delete(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_user_by_id_and_return_status_404_not_found(self):
        response = self.client.delete(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_detail_by_id_and_return_status_200_ok(self):
        response = self.client.put(self.url_with_id, self.payload_update_user_detail, format='json')

        updated_user = User.objects.get(id=self.user_id.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_user.username, self.payload_update_user_detail.get('username'))
        self.assertEqual(updated_user.email, self.payload_update_user_detail.get('email'))
    
    def test_update_user_detail_by_id_and_return_status_400_bad_request(self):
        response = self.client.put(self.url_with_id, self.invalid_payload_update_user_detail, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_detail_by_id_and_return_status_404_not_found(self):
        response = self.client.put(self.invalid_url_with_id, self.payload_update_user_detail, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_user_by_id_and_return_status_200_ok(self):
        response = self.client.patch(self.url_with_id, self.payload_patch, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_patch_user_by_id_and_return_status_404_not_found(self):
        response = self.client.patch(self.invalid_url_with_id, self.payload_patch, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_user_and_return_status_code_201_created(self):
        response = self.client.post(self.url, self.payload_post, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_and_return_status_code_400_bad_request(self):
        response = self.client.post(
            self.url, self.invalid_payload_post, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_and_return_status_code_404_not_found(self):
        response = self.client.post(
            self.invalid_url, self.payload_post, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_superuser_and_return_status_code_201_created(self):
        new_payload = copy.deepcopy(self.payload_post)
        new_payload['is_superuser'] = True

        response = self.client.post(self.url, new_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_superuser_and_return_status_code_400_bad_request(self):
        new_payload = copy.deepcopy(self.invalid_payload_post)
        new_payload['is_superuser'] = True

        response = self.client.post(self.url, new_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_and_return_status_code_404_not_found(self):
        new_payload = copy.deepcopy(self.invalid_payload_post)
        new_payload['is_superuser'] = True
        response = self.client.post(
            self.invalid_url, self.payload_post, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
