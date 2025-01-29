from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.address import Address
from ecommerce.users.serializers.address import (
    AddressDetailSerializer,
    AddressListCreateSerializer,
)

User = get_user_model()


class CommonSetUp(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_attributes = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'password_confirmation': 'testpassword123',
        }
        cls.user = User.objects.create_user(
            username=cls.user_attributes['username'],
            email=cls.user_attributes['email'],
            password=cls.user_attributes['password'],
        )
        cls.address_attributes = {
            'state': 'SP',
            'city': 'São Paulo',
            'neighborhood': 'Centro',
            'street': 'Rua das Flores',
            'number': '123',
            'complement': 'Apto 45',
            'cep': '01001-000',
            'user': cls.user,
        }
        cls.address = Address.objects.create(**cls.address_attributes)


class AddressListCreateSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = AddressListCreateSerializer(instance=cls.address)
        cls.data = cls.serializer.data

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
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = AddressDetailSerializer(instance=cls.address)
        cls.data = cls.serializer.data

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
