from rest_framework import serializers

from ecommerce.users.models.supplier import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'email',
        )
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
        }

        model = Supplier
