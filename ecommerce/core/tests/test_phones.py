from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ecommerce.core.models import Phone

User = get_user_model()


class PhoneTest(APITestCase):
    fixtures = ['phone.json', 'users.json']

    def setUp(self):
        self.pk = '07225864-afee-4f18-ba7f-45c71761ac7e'
        self.phone = Phone.objects.get(
            pk='7cdf12e4-fa09-42d4-9aad-b4d658e37622'
        )

    def test_get_all_phones_and_return_status_200_ok(self):
        response = self.client.get(reverse('phone-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)

    def test_get_all_phones_and_return_status_404_not_found(self):
        response = self.client.get('invalid_route')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_phone_by_id_and_return_status_200_ok(self):
        response = self.client.get(
            reverse('phone-detail', kwargs={'pk': str(self.phone.id)})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'id': str(self.phone.id),
                'DDD': self.phone.DDD,
                'number': self.phone.number,
                'user': str(self.phone.user.id),
                'supplier': self.phone.supplier,
            },
        )

    def test_get_phone_by_id_and_return_status_404_not_found(self):
        response = self.client.get(
            reverse('phone-detail', kwargs={'pk': str(self.pk)})
        )
        print(response)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_phone_by_id_and_return_status_204_no_content(self):
        response = self.client.delete(
            reverse('phone-detail', kwargs={'pk': str(self.phone.id)})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_phone_by_id_and_return_status_404_not_found(self):
        response = self.client.delete(
            reverse('phone-detail', kwargs={'pk': str(self.pk)})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_phone_by_id_and_return_status_200_ok(self):
        body = {'DDD': '41', 'number': '999999999', 'user': self.phone.user.id}

        response = self.client.put(
            reverse('phone-detail', kwargs={'pk': str(self.phone.id)}),
            body,
            format='json',
        )

        updated_phone = Phone.objects.get(id=self.phone.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_phone.id, self.phone.id)
        self.assertEqual(updated_phone.DDD, body['DDD'])
        self.assertEqual(updated_phone.number, body['number'])
        self.assertEqual(updated_phone.user.id, body['user'])

    def test_update_phone_by_id_and_return_status_404_not_found(self):
        body = {'DDD': '41', 'number': '999999999', 'user': self.phone.user.id}

        response = self.client.put(
            reverse('phone-detail', kwargs={'pk': str(self.pk)}),
            body,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_phone_by_id_and_return_status_200_ok(self):
        body = {'DDD': '21', 'number': '888888888', 'user': self.phone.user.id}

        response = self.client.patch(
            reverse('phone-detail', kwargs={'pk': str(self.phone.id)}),
            body,
            format='json',
        )

        patch_phone = Phone.objects.get(id=self.phone.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_phone.DDD, body['DDD'])
        self.assertEqual(patch_phone.number, body['number'])
        self.assertEqual(patch_phone.user.id, body['user'])

        self.assertEqual(patch_phone.id, self.phone.id)

    def test_patch_phone_by_id_and_return_status_404_not_found(self):
        body = {'DDD': '21', 'number': '888888888', 'user': self.phone.user.id}

        response = self.client.patch(
            reverse('phone-detail', kwargs={'pk': str(self.pk)}),
            body,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_phone_and_return_status_201_created(self):
        user = User.objects.get(pk='d19fb71e-7140-468b-899c-9b940da2476c')
        body = {'DDD': '42', 'number': '111111111', 'user': user.id}

        response = self.client.post(reverse('phone-list'), body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_phone_and_return_status_400_bad_request(self):
        user = User.objects.get(pk='d19fb71e-7140-468b-899c-9b940da2476c')
        body = {'DDD': '42', 'number': '', 'user': user.id}

        response = self.client.post(reverse('phone-list'), body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
