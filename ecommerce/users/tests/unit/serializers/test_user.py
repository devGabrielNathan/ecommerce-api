from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from ecommerce.users.serializers.user import (
    ResetPasswordSerializer,
    UserCreateAccountSerializer,
    UserDetailSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
)

User = get_user_model()


class CommonSetUp(ABC, APITestCase):
    @abstractmethod
    def setUp(self):
        pass


class UserCreateAccountSerializerUnitTest(CommonSetUp):
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


class UserDetailSerializerUnitTest(CommonSetUp):
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


class UserLoginSerializerUnitTest(CommonSetUp):
    def setUp(self):
        self.user_attributes = {
            'email': 'leonardodavinci@gmail.com',
            'password': 'leonardo1452',
        }
        self.user = User.objects.create(
            email=self.user_attributes['email'],
            password=make_password(self.user_attributes['password']),
        )
        self.serializer = UserLoginSerializer(data=self.user_attributes)
        self.serializer.is_valid(raise_exception=True)
        self.data = self.serializer.validated_data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(), ['id', 'access', 'refresh', 'email', 'password']
        )

    def test_email_field_content(self):
        self.assertEqual(self.data['email'], self.user_attributes['email'])

    def test_password_field_content(self):
        self.assertEqual(
            self.data['password'], self.user_attributes['password']
        )

    def test_email_not_found(self):
        payload = {'email': ''}
        user = User.objects.filter(email=payload['email']).first()
        self.assertIsNone(user)

    def test_password_incorrect(self):
        payload = {'email': 'admin@admin.com', 'password': 'gabriel123'}
        user = User.objects.filter(email=payload['email']).first()

        self.assertFalse(user.check_password(payload['password']))


class UserLogoutSerializerUnitTest(CommonSetUp):
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
        self.refresh = {
            'refresh': str(RefreshToken.for_user(self.user)),
        }
        self.serializer = UserLogoutSerializer(data=self.refresh)
        self.serializer.is_valid(raise_exception=True)
        self.data = self.serializer.validated_data

    def test_refresh_field_content(self):
        self.assertEqual(self.data['refresh'], self.refresh['refresh'])


class ResetPasswordSerializerUnitTest(CommonSetUp):
    def setUp(self):
        self.reset_password_attributes = {
            'old_password': 'oldpassword123',
            'new_password': 'newpassword',
            'password_confirmation': 'newpassword',
        }
        self.reset_password = User.objects.update(
            password=self.reset_password_attributes['new_password'],
        )
        self.serializer = ResetPasswordSerializer(
            data=self.reset_password_attributes
        )
        self.serializer.is_valid(raise_exception=True)
        self.data = self.serializer.validated_data

    def test_contains_expected_fields(self):
        self.assertCountEqual(
            self.data.keys(),
            ['old_password', 'new_password', 'password_confirmation'],
        )

    def test_old_password_field_content(self):
        self.assertEqual(
            self.data['old_password'],
            self.reset_password_attributes['old_password'],
        )

    def test_new_password_field_content(self):
        self.assertEqual(
            self.data['new_password'],
            self.reset_password_attributes['new_password'],
        )

    def test_password_confirmation_field_content(self):
        self.assertEqual(
            self.data['password_confirmation'],
            self.reset_password_attributes['password_confirmation'],
        )

    def test_passwords_do_not_match(self):
        payload = {
            'old_password': 'oldpassword123',
            'new_password': 'newpassword',
            'password_confirmation': 'newpassword123',
        }

        self.assertNotEqual(
            payload['new_password'], payload['password_confirmation']
        )

    def test_update_password(self):
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
        payload = {
            'old_password': 'testpassword123',
            'new_password': 'newpassword',
            'password_confirmation': 'newpassword',
        }
        serializer = ResetPasswordSerializer(instance=self.user, data=payload)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertTrue(user.check_password(payload['new_password']))
        self.assertFalse(user.check_password(payload['old_password']))
