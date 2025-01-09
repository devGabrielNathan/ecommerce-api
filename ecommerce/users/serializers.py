from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        label=_('Password'),
        min_length=8,
        max_length=150,
        write_only=True,
        error_messages={
            'min_length': _(
                'The password must contain at least 8 characters.'
            ),
            'max_length': _('The password cannot exceed 150 characters.'),
        },
    )
    password_confirmation = serializers.CharField(
        label=_('Password Confirmation'),
        min_length=8,
        max_length=150,
        write_only=True,
        error_messages={
            'min_length': _(
                'The password must contain at least 8 characters.'
            ),
            'max_length': _('The password cannot exceed 150 characters.'),
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
            raise ValidationError({'password_confirmation': _('Passwords do not match')})
        return data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
