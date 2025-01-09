from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ecommerce.core.models import Address

User = get_user_model()


class AddressTest(APITestCase):
    fixtures = ['addresses.json', 'users.json']

    def setUp(self):
        self.invalid_pk_address = 'ceee9266-9e82-459b-a0a5-f83e2096db82'
        self.address = Address.objects.get(pk='faafa8bd-a924-473f-86f1-6b12b2dfe3ec')

    def test_get_all_address_and_return_status_200_ok(self):
        response = self.client.get(reverse('address-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)

    def test_get_all_address_and_return_status_404_not_found(self):
        response = self.client.get('/invalid_route/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_address_by_id_and_return_status_200_ok(self):
        response = self.client.get(
            reverse('address-detail', kwargs={'pk': str(self.address.id)})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_address_by_id_and_return_status_404_not_found(self):
        response = self.client.get(
            reverse(
                'address-detail', kwargs={'pk': str(self.invalid_pk_address)}
            )
        )
        print(response)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_address_by_id_and_return_status_204_no_content(self):
        response = self.client.delete(
            reverse('address-detail', kwargs={'pk': str(self.address.id)})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_address_by_id_and_return_status_404_not_found(self):
        response = self.client.delete(
            reverse(
                'address-detail', kwargs={'pk': str(self.invalid_pk_address)}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_address_by_id_and_return_status_200_ok(self):
        body = {
            'state': 'MA',
            'city': 'Imperatriz',
            'neighborhood': 'Santa Rita',
            'street': 'Rua Imperatriz Leopoldina',
            'number': '456',
            'complement': 'Apto. 1',
            'cep': '65919250',
            'user': str(self.address.user.id),
        }

        response = self.client.put(
            reverse('address-detail', kwargs={'pk': str(self.address.id)}),
            body,
            format='json',
        )

        updated_address = Address.objects.get(id=self.address.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_address.id, self.address.id)
        self.assertEqual(updated_address.state, body.get('state'))
        self.assertEqual(updated_address.city, body.get('city'))
        self.assertEqual(
            updated_address.neighborhood, body.get('neighborhood')
        )
        self.assertEqual(updated_address.street, body.get('street'))
        self.assertEqual(updated_address.number, body.get('number'))
        self.assertEqual(updated_address.complement, body.get('complement'))
        self.assertEqual(updated_address.cep, body.get('cep'))
        self.assertEqual(str(updated_address.user.id), body.get('user'))

    def test_update_address_by_id_and_return_status_404_not_found(self):
        body = {
            'state': 'MA',
            'city': 'Imperatriz',
            'neighborhood': 'Santa Rita',
            'street': 'Rua Imperatriz Leopoldina',
            'number': '456',
            'complement': 'Apto. 1',
            'cep': '65919250',
            'user': str(self.address.user.id),
        }

        response = self.client.put(
            reverse(
                'phone-detail', kwargs={'pk': str(self.invalid_pk_address)}
            ),
            body,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_address_by_id_and_return_status_200_ok(self):
        body = {
            'city': 'Imperatriz',
            'street': 'Rua Imperatriz Leopoldina',
            'user': str(self.address.user.id),
        }

        response = self.client.patch(
            reverse('address-detail', kwargs={'pk': str(self.address.id)}),
            body,
            format='json',
        )

        patch_address = Address.objects.get(id=self.address.id)

        self.assertEqual(patch_address.id, self.address.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_address.city, body.get('city'))
        self.assertEqual(patch_address.street, body.get('street'))

        self.assertEqual(patch_address.state, self.address.state)
        self.assertEqual(patch_address.neighborhood, self.address.neighborhood)
        self.assertEqual(patch_address.number, self.address.number)
        self.assertEqual(patch_address.complement, self.address.complement)
        self.assertEqual(patch_address.cep, self.address.cep)
        self.assertEqual(str(patch_address.user.id), str(self.address.user.id))

    def test_patch_address_by_id_and_return_status_404_not_found(self):
        body = {
            'state': 'MA',
            'city': 'Imperatriz',
            'neighborhood': 'Santa Rita',
            'street': 'Rua Imperatriz Leopoldina',
            'number': '789',
            'complement': 'Apto. 1',
            'cep': '65919250',
            'user': str(self.address.user.id),
        }

        response = self.client.patch(
            reverse(
                'address-detail', kwargs={'pk': str(self.invalid_pk_address)}
            ),
            body,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_address_and_return_status_201_created(self):
        user = User.objects.get(pk='d19fb71e-7140-468b-899c-9b940da2476c')
        body = {
            'state': 'SP',
            'city': 'São Paulo',
            'neighborhood': 'Centro',
            'street': 'Rua das Flores',
            'number': '123',
            'complement': 'Apto 45',
            'cep': '01001000',
            'user': str(user.id),
        }

        response = self.client.post(
            reverse('address-list'), body, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_address_and_return_status_400_bad_request(self):
        user = User.objects.get(pk='d19fb71e-7140-468b-899c-9b940da2476c')
        body = {
            'state': '',
            'city': '',
            'neighborhood': '',
            'street': '',
            'number': '',
            'complement': '',
            'cep': '',
            'user': str(user.id),
        }

        response = self.client.post(
            reverse('address-list'), body, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
