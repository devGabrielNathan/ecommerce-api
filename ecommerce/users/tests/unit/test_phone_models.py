from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.phone import Phone

User = get_user_model()


class PhoneUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.phone = Phone.objects.create(DDD='41', number='999999999')

    def test_format_str_magic_method(self):
        expected = f'{self.phone.DDD} {self.phone.number}'

        self.assertEqual(str(self.phone), expected)
