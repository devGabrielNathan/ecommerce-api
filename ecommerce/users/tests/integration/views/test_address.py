from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ecommerce.users.models.address import Address

User = get_user_model()


class CommonSetUp(APITestCase):
    fixtures = ['users.json', 'addresses.json']

    def setUp(self):
        self.user_id = User.objects.get(
            pk='d19fb71e-7140-468b-899c-9b940da2476c'
        )
        self.client.force_authenticate(user=self.user_id)

        self.address_id = Address.objects.get(
            pk='faafa8bd-a924-473f-86f1-6b12b2dfe3ec'
        )
        self.invalid_address_id = 'ceee9266-9e82-459b-a0a5-f83e2096db82'
        self.url = reverse('address-list')
        self.invalid_url = 'invalid-url/'

        self.url_with_id = reverse(
            'address-detail', kwargs={'pk': str(self.address_id.id)}
        )
        self.invalid_url_with_id = f'addresses/{str(self.invalid_address_id)}/'


class AddressDetailIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.payload_update = {
            'state': 'TE',
            'city': 'Teste',
            'neighborhood': 'Teste',
            'street': 'Teste',
            'number': '123',
            'complement': 'Teste',
            'cep': '12345678',
            'user': str(self.user_id.id),
        }
        self.invalid_payload_update = {
            'state': 'TE',
            'city': 'Teste',
            'neighborhood': 'Teste',
            'street': 'Teste',
            'number': '123',
            'complement': 'Teste',
            'cep': '12345678',
        }
        self.payload_patch = {'city': 'Imperatriz', 'street': 'Rua Imper'}

    def test_get_address_by_id_and_return_status_200_ok(self):
        response = self.client.get(self.url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_address_by_id_and_return_status_404_not_found(self):
        response = self.client.get(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_address_by_id_and_return_status_200_ok(self):
        response = self.client.put(
            self.url_with_id, self.payload_update, format='json'
        )

        updated_address = Address.objects.get(id=self.address_id.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_address.id, self.address_id.id)
        self.assertEqual(
            updated_address.state, self.payload_update.get('state')
        )
        self.assertEqual(updated_address.city, self.payload_update.get('city'))
        self.assertEqual(
            updated_address.neighborhood,
            self.payload_update.get('neighborhood'),
        )
        self.assertEqual(
            updated_address.street, self.payload_update.get('street')
        )
        self.assertEqual(
            updated_address.number, self.payload_update.get('number')
        )
        self.assertEqual(
            updated_address.complement, self.payload_update.get('complement')
        )
        self.assertEqual(updated_address.cep, self.payload_update.get('cep'))
        self.assertEqual(
            str(updated_address.user.id), self.payload_update.get('user')
        )

    def test_update_address_by_id_and_return_status_404_not_found(self):
        response = self.client.put(
            self.invalid_url_with_id, self.payload_update, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_address_by_id_and_return_status_200_ok(self):
        response = self.client.patch(
            self.url_with_id, self.payload_patch, format='json'
        )

        patch_address = Address.objects.get(id=self.address_id.id)

        self.assertEqual(patch_address.id, self.address_id.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_address.city, self.payload_patch.get('city'))
        self.assertEqual(
            patch_address.street, self.payload_patch.get('street')
        )
        self.assertEqual(patch_address.state, self.address_id.state)
        self.assertEqual(
            patch_address.neighborhood, self.address_id.neighborhood
        )
        self.assertEqual(patch_address.number, self.address_id.number)
        self.assertEqual(patch_address.complement, self.address_id.complement)
        self.assertEqual(patch_address.cep, self.address_id.cep)
        self.assertEqual(
            str(patch_address.user.id), str(self.address_id.user.id)
        )

    def test_patch_address_by_id_and_return_status_404_not_found(self):
        response = self.client.patch(
            self.invalid_url_with_id, self.payload_patch, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_address_by_id_and_return_status_204_no_content(self):
        response = self.client.delete(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_address_by_id_and_return_status_404_not_found(self):
        response = self.client.delete(self.invalid_url_with_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AddressCreateIntegrationTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.payload = {
            'state': 'TE',
            'city': 'Teste',
            'neighborhood': 'Teste',
            'street': 'Teste',
            'number': '123',
            'complement': 'Teste',
            'cep': '12345678',
            'user': str(self.user_id.id),
        }
        self.invalid_payload = {
            'state': 'TE',
            'city': 'Teste',
            'neighborhood': 'Teste',
            'street': 'Teste',
            'number': '123',
            'complement': 'Teste',
            'cep': '12345678',
        }

    def test_post_address_and_return_status_201_created(self):
        response = self.client.post(self.url, self.payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_address_and_return_status_400_bad_request(self):
        response = self.client.post(
            self.url, self.invalid_payload, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_address_and_return_status_404_not_found(self):
        response = self.client.post(
            self.invalid_url, self.payload, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
