from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
            'user',
            'supplier',
            )
        
        model = Address

    def validate(self, data):
        user = self.data.get('user')
        supplier = self.data.get('supplier')

        if user and supplier:
            raise ValidationError('An address cannot belong to both a user and a supplier')
        
        if not user and not supplier:
            raise ValidationError('The address must contain a user or a supplier')
        
        return data


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'DDD',
            'number',
            'user',
            'supplier',
            )
        
        model = Phone

    def validate(self, attrs):
        user = attrs.get('user')
        supplier = attrs.get('supplier')

        if user and supplier:
            raise ValidationError('An phone cannot belong to both a user and a supplier')
        
        if not user and not supplier:
            raise ValidationError('The phone must contain a user or a supplier')
        
        return attrs
