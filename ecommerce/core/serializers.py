from rest_framework import serializers
from ecommerce.core import models


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
        
        model = models.Address


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'DDD',
            'number',
            'user',
            'supplier',
            )
        
        model = models.Phone
