from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.orders.models.order import Order

User = get_user_model()


class OrderUnitTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='UserTest', email='teste@gmail.com', password='123456789'
        )
        cls.order = Order.objects.create(user=cls.user)

    def test_str_magic_method(self):
        expected = f'{self.order.id}'

        self.assertEqual(str(self.order), expected)
