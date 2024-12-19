from rest_framework import serializers
from ecommerce.core.models import Address, Phone


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'state',
            'city',
            'neighborhood',
            'street',
            'number',
            'complement',
            'cep',
            )
        
        model = Address


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'DDD',
            'number',
            'user',
            'supplier',
            )
        
        model = Phone
