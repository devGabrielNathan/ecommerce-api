from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.address import Address
from ecommerce.users.models.phone import Phone

User = get_user_model()


class AddressTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            state='MA',
            city='Imperatriz',
            neighborhood='Santa Rita',
            street='Rua Imperatriz Leopoldina',
            number='456',
            complement='Apto. 1',
            cep='65919250',
        )
        cls.address_without_complement = Address.objects.create(
            state='MA',
            city='Imperatriz',
            neighborhood='Santa Rita',
            street='Rua Imperatriz Leopoldina',
            number='456',
            cep='65919250',
        )

    def test_format_str_magic_method_with_complement(self):
        expected = (
            f'{self.address.street}, {self.address.number}, {self.address.complement}, '
            f'{self.address.neighborhood}, {self.address.city} - {self.address.state}, {self.address.cep}'
        )

        self.assertEqual(str(self.address), expected)

    def test_format_str_magic_method_without_complement(self):
        expected = (
            f'{self.address_without_complement.street} - {self.address_without_complement.neighborhood}, '
            f'{self.address_without_complement.city} - {self.address_without_complement.state}, {self.address_without_complement.cep}'
        )

        self.assertEqual(str(self.address_without_complement), expected)


class PhoneUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.phone = Phone.objects.create(DDD='41', number='999999999')

    def test_format_str_magic_method(self):
        expected = f'{self.phone.DDD} {self.phone.number}'

        self.assertEqual(str(self.phone), expected)
