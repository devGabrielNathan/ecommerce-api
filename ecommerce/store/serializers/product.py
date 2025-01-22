from rest_framework import serializers

from ecommerce.store.models.product import Product
from ecommerce.store.models.subcategory import Subcategory


class ProductListSerializer(serializers.ModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(), required=False
    )

    class Meta:
        fields = ['id', 'brand', 'name', 'description', 'price', 'quantity', 'status', 'subcategory']
        model = Product

class ProductDetailSerializer(serializers.ModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(), required=False
    )

    class Meta:
        fields = ['id', 'brand', 'name', 'description', 'price', 'quantity', 'status', 'subcategory']
        model = Product

