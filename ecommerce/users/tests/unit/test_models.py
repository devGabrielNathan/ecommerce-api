from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class UserTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='UserTest',
            email='teste@gmail.com',
            password='123456789'
        )

    def test_format_str_magic_method(self):
        expected = f'{self.user.username} - {self.user.email}'

        self.assertEqual(str(self.user), expected)
