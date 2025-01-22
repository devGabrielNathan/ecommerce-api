from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.address import Address
from ecommerce.users.serializers.address import (
    AddressCreateSerializer,
    AddressDetailSerializer,
)

User = get_user_model()


class CommonSetUp(APITestCase):
    def setUp(self):
        self.user_attributes = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'password_confirmation': 'testpassword123',
        }
        self.user = User.objects.create_user(
            username=self.user_attributes['username'],
            email=self.user_attributes['email'],
            password=self.user_attributes['password'],
        )
        self.address_attributes = {
            'state': 'SP',
            'city': 'São Paulo',
            'neighborhood': 'Centro',
            'street': 'Rua das Flores',
            'number': '123',
            'complement': 'Apto 45',
            'cep': '01001-000',
            'user': self.user,
        }
        self.address = Address.objects.create(**self.address_attributes)


class AddressCreateSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = AddressCreateSerializer(instance=self.address)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            [
                'id',
                'state',
                'city',
                'neighborhood',
                'street',
                'number',
                'complement',
                'cep',
                'user',
            ],
        )

    def test_state_field_content(self):
        self.assertEqual(self.data['state'], self.address_attributes['state'])

    def test_city_field_content(self):
        self.assertEqual(self.data['city'], self.address_attributes['city'])

    def test_neighborhood_field_content(self):
        self.assertEqual(
            self.data['neighborhood'], self.address_attributes['neighborhood']
        )

    def test_street_field_content(self):
        self.assertEqual(
            self.data['street'], self.address_attributes['street']
        )

    def test_number_field_content(self):
        self.assertEqual(
            self.data['number'], self.address_attributes['number']
        )

    def test_complement_field_content(self):
        self.assertEqual(
            self.data['complement'], self.address_attributes['complement']
        )

    def test_cep_field_content(self):
        self.assertEqual(self.data['cep'], self.address_attributes['cep'])


class AddressDetailSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = AddressDetailSerializer(instance=self.address)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            [
                'id',
                'state',
                'city',
                'neighborhood',
                'street',
                'number',
                'complement',
                'cep',
                'user',
            ],
        )

    def test_state_field_content(self):
        self.assertEqual(self.data['state'], self.address_attributes['state'])

    def test_city_field_content(self):
        self.assertEqual(self.data['city'], self.address_attributes['city'])

    def test_neighborhood_field_content(self):
        self.assertEqual(
            self.data['neighborhood'], self.address_attributes['neighborhood']
        )

    def test_street_field_content(self):
        self.assertEqual(
            self.data['street'], self.address_attributes['street']
        )

    def test_number_field_content(self):
        self.assertEqual(
            self.data['number'], self.address_attributes['number']
        )

    def test_complement_field_content(self):
        self.assertEqual(
            self.data['complement'], self.address_attributes['complement']
        )

    def test_cep_field_content(self):
        self.assertEqual(self.data['cep'], self.address_attributes['cep'])
