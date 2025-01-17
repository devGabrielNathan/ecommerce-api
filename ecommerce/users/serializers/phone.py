from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ecommerce.users.models.phone import Phone
from ecommerce.users.models.supplier import Supplier

User = get_user_model()


class PhoneCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), required=False
    )

    class Meta:
        fields = (
            'id',
            'DDD',
            'number',
            'user',
            'supplier',
        )

        model = Phone

    def validate(self, data):
        user = data.get('user')
        supplier = data.get('supplier')

        if user and supplier:
            raise ValidationError(
                'An phone cannot belong to both a user and a supplier'
            )

        if not user and not supplier:
            raise ValidationError(
                'The phone must contain a user or a supplier'
            )

        return data


class PhoneDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), required=False
    )

    class Meta:
        fields = (
            'id',
            'DDD',
            'number',
            'user',
            'supplier',
        )

        model = Phone

    def validate(self, data):
        user = data.get('user')
        supplier = data.get('supplier')

        if user and supplier:
            raise ValidationError(
                'An phone cannot belong to both a user and a supplier'
            )

        if not user and not supplier:
            raise ValidationError(
                'The phone must contain a user or a supplier'
            )

        return data
