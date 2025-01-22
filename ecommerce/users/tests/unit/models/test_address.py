from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.address import Address

User = get_user_model()


class AddressUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='UserTest', email='teste@gmail.com', password='123456789'
        )
        cls.address = Address.objects.create(
            state='MA',
            city='Imperatriz',
            neighborhood='Santa Rita',
            street='Rua Imperatriz Leopoldina',
            number='456',
            complement='Apto. 1',
            cep='65919250',
            user=cls.user,
        )
        cls.address_without_complement = Address.objects.create(
            state='MA',
            city='Imperatriz',
            neighborhood='Santa Rita',
            street='Rua Imperatriz Leopoldina',
            number='456',
            cep='65919250',
            user=cls.user,
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
