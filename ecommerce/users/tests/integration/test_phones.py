from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from ecommerce.users.models.phone import Phone

User = get_user_model()


class PhoneIntegrationTest(APITestCase):
    fixtures = ['users.json', 'phones.json']

    def setUp(self):
        self.user_id = User.objects.get(
            pk='d19fb71e-7140-468b-899c-9b940da2476c'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user_id)
        self.invalid_pk_phone = '07225864-afee-4f18-ba7f-45c71761ac7e'

        self.phone_id = Phone.objects.get(
            pk='7cdf12e4-fa09-42d4-9aad-b4d658e37622'
        )
        self.invalid_phone_id = 'c0217bd2-d272-421b-85b7-4074c32ae673'

        self.url = reverse('phone-list')
        self.invalid_url = 'invalid-url/'

        self.url_with_id = reverse(
            'phone-detail', kwargs={'pk': str(self.phone_id.id)}
        )
        self.invalid_url_with_id = (
            f'phones/{str(self.invalid_phone_id)}/'
        )

        self.payload_patch = {
            'DDD': '99'
        }
        self.payload_update = {
            'DDD': '99',
            'number': '999999999',
            'user': str(self.user_id.id),
        }
        self.invalid_payload_update = {
            'DDD': '99',
            'number': '999999999'
        }
        self.payload_post = {
            'DDD': '11',
            'number': '98754321',
            'user': str(self.user_id.id),
        }
        self.invalid_payload_post = {
            'DDD': '11',
            'number': '98754321'
        }

    def test_get_phone_by_id_and_return_status_200_ok(self):
        response = self.client.get(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_phone_by_id_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_phone_by_id_and_return_status_204_no_content(self):
        response = self.client.delete(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_phone_by_id_and_return_status_404_not_found(self):
        response = self.client.delete(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_phone_by_id_and_return_status_200_ok(self):
        response = self.client.put(self.url_with_id, self.payload_update, format='json')

        updated_phone = Phone.objects.get(id=self.phone_id.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_phone.id, self.phone_id.id)
        self.assertEqual(updated_phone.DDD, self.payload_update.get('DDD'))
        self.assertEqual(updated_phone.number, self.payload_update.get('number'))
        self.assertEqual(str(updated_phone.user.id), self.payload_update.get('user'))

    def test_update_phone_by_id_and_return_status_404_not_found(self):
        response = self.client.put(self.invalid_url_with_id, self.payload_update, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_phone_by_id_and_return_status_200_ok(self):
        response = self.client.patch(self.url_with_id, self.payload_patch, format='json')

        patch_phone = Phone.objects.get(id=str(self.phone_id.id))

        self.assertEqual(str(patch_phone.id), str(self.phone_id.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_phone.DDD, self.payload_patch.get('DDD'))


    def test_patch_phone_by_id_and_return_status_404_not_found(self):
        response = self.client.patch(self.invalid_url_with_id, self.payload_patch, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_phone_and_return_status_201_created(self):
        response = self.client.post(self.url, self.payload_update, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_phone_and_return_status_400_bad_request(self):
        response = self.client.post(self.url, self.invalid_payload_post, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_phone_and_return_status_404_not_found(self):
        response = self.client.post(self.invalid_url, self.payload_post, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
