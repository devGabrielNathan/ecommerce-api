from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from ecommerce.users.serializers.user import (
    UserCreateAccountSerializer,
    UserDetailSerializer,
)

User = get_user_model()


class UserCreateAccountSerializerUnitTest(APITestCase):
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
        self.serializer = UserCreateAccountSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'username', 'email'])

    def test_username_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.user_attributes['username'])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.user_attributes['email'])

    def test_create_user(self):
        payload = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'password_confirmation': 'newpassword123',
        }
        serializer = UserCreateAccountSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, payload['username'])
        self.assertEqual(user.email, payload['email'])
        self.assertTrue(user.check_password(payload['password']))

    def test_passwords_do_not_match(self):
        payload = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password',
            'password_confirmation': '',
        }
        self.assertNotEqual(
            payload['password'], payload['password_confirmation']
        )


class UserDetailSerializerUnitTest(APITestCase):
    def setUp(self):
        self.user_attributes = {'username': 'teste', 'email': 'test@gmail.com'}
        self.user = User.objects.create_user(
            username=self.user_attributes['username'],
            email=self.user_attributes['email'],
        )
        self.serializer = UserDetailSerializer(instance=self.user)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(self.data.keys(), ['id', 'username', 'email'])

    def test_username_field_content(self):
        self.assertEqual(
            self.data['username'], self.user_attributes['username']
        )

    def test_email_field_content(self):
        self.assertEqual(self.data['email'], self.user_attributes['email'])
