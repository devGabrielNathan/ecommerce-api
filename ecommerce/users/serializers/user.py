from uuid import uuid4

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

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
            'id': {'read_only': True},
            'username': {'required': True},
            'email': {'required': True},
        }
        model = User

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate(self, data):
        if self.context['request'].method == 'POST':
            if data['password'] != data['password_confirmation']:
                raise ValidationError({
                    'password_confirmation': 'Passwords do not match.'
                })
            return data



class UserLoginSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid4, read_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    email = serializers.EmailField(
        required=True,
        write_only=True,
        error_messages={'required': 'You need to enter the email.'},
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={'required': 'You need to enter the password.'},
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(email=email).first()

        if not user or not user.check_password(password):
            raise serializers.ValidationError({
                'email': 'User with this email was not found.'
                if not user
                else 'Incorrect password.'
            })

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        data['id'] = user.id
        data['access'] = access
        data['refresh'] = refresh

        return data


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        error_messages={'required': 'You need to enter the refresh token.'}
    )

    def validate(self, data):
        refresh = data.get('refresh')
        refresh_token = RefreshToken(refresh)
        refresh_token.blacklist()

        data['refresh'] = refresh

        return data
    
class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        label='Old Password',
        min_length=8,
        max_length=150,
        write_only=True,
        required=True,
        error_messages={
            'min_length': 'The password must contain at least 8 characters.',
            'max_length': 'The password cannot exceed 150 characters.',
        },
    )
    new_password = serializers.CharField(
        label='Password',
        min_length=8,
        max_length=150,
        write_only=True,
        required=True,
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
        required=True,
        error_messages={
            'min_length': 'The password must contain at least 8 characters.',
            'max_length': 'The password cannot exceed 150 characters.',
        },
    )

    def update(self, instance, validated_data):
        old_password = validated_data.get('old_password')
        
        if not instance.check_password(old_password):
            raise ValidationError({'old_password': 'Old password is incorrect.'})
        
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance
    
    def validate(self, data):
        if data['new_password'] != data['password_confirmation']:
            raise ValidationError({
                'password_confirmation': 'Passwords do not match.'
            })
        return data
