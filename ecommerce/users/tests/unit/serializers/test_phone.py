from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.phone import Phone
from ecommerce.users.serializers.phone import (
    PhoneCreateSerializer,
    PhoneDetailSerializer,
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

        self.phone_attributes = {
            'DDD': '22',
            'number': '999999999',
            'user': self.user,
        }
        self.phone = Phone.objects.create(**self.phone_attributes)


class PhoneCreateSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = PhoneCreateSerializer(instance=self.phone)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(), ['id', 'DDD', 'number', 'user']
        )

    def test_ddd_field_content(self):
        self.assertEqual(self.data['DDD'], self.phone_attributes['DDD'])

    def test_number_field_content(self):
        self.assertEqual(self.data['number'], self.phone_attributes['number'])

    # def test_create_phone(self):
    #     payload = {
    #         'DDD': '22',
    #         'number': '999999999',
    #         'user': self.user
    #     }
    #     serializer = PhoneCreateSerializer(data=payload)
    #     # import pdb; pdb.set_trace()
    #     self.assertTrue(serializer.is_valid())
    #     phone = serializer.save()
    #     self.assertEqual(phone.DDD, payload['DDD'])
    #     self.assertEqual(phone.number, payload['number'])
    #     self.assertTrue(phone.check_user(payload['user']))


class PhoneDetailSerializerUnitTest(CommonSetUp):
    def setUp(self):
        super().setUp()

        self.serializer = PhoneDetailSerializer(instance=self.phone)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(), ['id', 'DDD', 'number', 'user']
        )

    def test_ddd_field_content(self):
        self.assertEqual(self.data['DDD'], self.phone_attributes['DDD'])

    def test_number_field_content(self):
        self.assertEqual(self.data['number'], self.phone_attributes['number'])
