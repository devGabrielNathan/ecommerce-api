from django.contrib.auth import get_user_model
from rest_framework import serializers

from ecommerce.users.models.phone import Phone

User = get_user_model()


class PhoneCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )

    class Meta:
        fields = (
            'id',
            'DDD',
            'number',
            'user',
        )

        model = Phone


class PhoneDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        fields = (
            'id',
            'DDD',
            'number',
            'user',
        )

        model = Phone
