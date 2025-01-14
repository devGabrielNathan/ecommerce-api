from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        label='Password',
        min_length=8,
        max_length=150,
        write_only=True,
        error_messages={
            'min_length': 'The password must contain at least 8 characters.',
            'max_length': 'The password cannot exceed 150 characters.',
        },
    )
    password_confirmation = serializers.CharField(
        label='Password Confirmation',
        min_length=8,
        max_length=150,
        write_only=True,
        error_messages={
            'min_length': 'The password must contain at least 8 characters.',
            'max_length': 'The password cannot exceed 150 characters.',
        },
    )

    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'password',
            'password_confirmation',
        )
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }
        model = User

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise ValidationError({
                'password_confirmation': 'Passwords do not match.'
            })
        return data


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        error_messages={'required': 'You need to enter the refresh token.'}
    )
