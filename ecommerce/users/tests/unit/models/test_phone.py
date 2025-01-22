from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.phone import Phone

User = get_user_model()


class PhoneUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='UserTest', email='teste@gmail.com', password='123456789'
        )
        cls.phone = Phone.objects.create(
            DDD='41', number='999999999', user=cls.user
        )

    def test_format_str_magic_method(self):
        expected = f'{self.phone.DDD} {self.phone.number}'

        self.assertEqual(str(self.phone), expected)
