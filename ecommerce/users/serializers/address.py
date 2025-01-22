from django.contrib.auth import get_user_model
from rest_framework import serializers

from ecommerce.users.models.address import Address

User = get_user_model()


class AddressListCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )

    class Meta:
        fields = (
            'id',
            'state',
            'city',
            'neighborhood',
            'street',
            'number',
            'complement',
            'cep',
            'user',
        )

        model = Address


class AddressDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        fields = (
            'id',
            'state',
            'city',
            'neighborhood',
            'street',
            'number',
            'complement',
            'cep',
            'user',
        )

        model = Address
