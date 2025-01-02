from uuid import uuid4

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ecommerce.core.models import Phone

User = get_user_model()


class PhoneTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=uuid4(),
            username='testuser',
            email='testuser@example.com',
        )
        self.phone = Phone.objects.create(
            id=uuid4(),
            DDD='21',
            number='999999999',
            user=self.user,
            supplier=None,
        )

    def test_get_all_phones_and_return_status_200_ok(self):
        response = self.client.get(reverse('phone-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()[0],
            {
                'id': str(self.phone.id),
                'DDD': self.phone.DDD,
                'number': self.phone.number,
                'user': str(self.phone.user.id),
                'supplier': self.phone.supplier,
            },
        )

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

    def test_delete_phone_by_id_and_return_status_204_no_content(self):
        response = self.client.delete(
            reverse('phone-detail', kwargs={'pk': str(self.phone.id)})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_phone_by_id_and_return_status_200_ok(self):
        body = {'DDD': '41', 'number': '999999999', 'user': self.user.id}

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

    def test_patch_phone_by_id_and_return_status_200_ok(self):
        body = {'DDD': '21', 'number': '888888888', 'user': self.user.id}

        response = self.client.patch(
            reverse('phone-detail', kwargs={'pk': str(self.phone.id)}),
            body,
            format='json',
        )

        updated_phone = Phone.objects.get(id=self.phone.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_phone.DDD, body['DDD'])
        self.assertEqual(updated_phone.number, body['number'])
        self.assertEqual(updated_phone.user.id, body['user'])

        self.assertEqual(updated_phone.id, self.phone.id)

    def test_post_phone_and_return_status_201_created(self):
        body = {'DDD': '42', 'number': '111111111', 'user': self.user.id}

        response = self.client.post(reverse('phone-list'), body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
