from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.models.phone import Phone
from ecommerce.users.serializers.phone import (
    PhoneDetailSerializer,
    PhoneListCreateSerializer,
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

        cls.phone_attributes = {
            'DDD': '22',
            'number': '999999999',
            'user': cls.user,
        }
        cls.phone = Phone.objects.create(**cls.phone_attributes)


class PhoneListCreateSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = PhoneListCreateSerializer(instance=cls.phone)
        cls.data = cls.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(), ['id', 'DDD', 'number', 'user']
        )

    def test_ddd_field_content(self):
        self.assertEqual(self.data['DDD'], self.phone_attributes['DDD'])

    def test_number_field_content(self):
        self.assertEqual(self.data['number'], self.phone_attributes['number'])

    def test_user_field_content(self):
        self.assertEqual(self.data['user'], self.phone_attributes['user'].id)


class PhoneDetailSerializerUnitTest(CommonSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.serializer = PhoneDetailSerializer(instance=cls.phone)
        cls.data = cls.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(), ['id', 'DDD', 'number', 'user']
        )

    def test_ddd_field_content(self):
        self.assertEqual(self.data['DDD'], self.phone_attributes['DDD'])

    def test_number_field_content(self):
        self.assertEqual(self.data['number'], self.phone_attributes['number'])

    def test_user_field_content(self):
        self.assertEqual(self.data['user'], self.phone_attributes['user'].id)
