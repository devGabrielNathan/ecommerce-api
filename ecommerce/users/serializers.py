from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.validators import ValidationError

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
    label=_("Username"),
    max_length=150,
    validators=[UniqueValidator(queryset=User.objects.all())],
    help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    ),
    error_messages={
        "unique": _("A user with that username already exists."),
        }
    )
    email = serializers.EmailField(
        label=_("Email Address"),
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        error_messages={
            "unique": _("A user with that email address already exists."),
        }
    )
    password1 = serializers.CharField(
        label=_("Password"),
        min_length=8,
        max_length=150,
        write_only=True,
        error_messages={
            'min_length': _("The password must contain at least 8 characters."),
            'max_length': _("The password cannot exceed 150 characters."),
        }
    )
    password2 = serializers.CharField(
        label=_("Password Confirmation"),
        min_length=8,
        max_length=150,
        write_only=True,
        error_messages={
            'min_length': _("The password must contain at least 8 characters."),
            'max_length': _("The password cannot exceed 150 characters."),
        }
    )

    def validate(self, data):
        type(data)
        if data['password1'] != data['password2']:
            raise ValidationError({
                "password2": _("Passwords do not match")
                }
            )
        return data
    
    def create(self, validated_data):
        type(validated_data)
        validated_data.pop('password2', None)
        password = validated_data.pop("password1")
        user = User.objects.create_user(password=password, **validated_data)
        user.save()
        return user
