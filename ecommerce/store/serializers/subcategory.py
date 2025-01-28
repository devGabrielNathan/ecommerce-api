from rest_framework import serializers

from ecommerce.store.models.subcategory import Subcategory


class SubcategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'status', 'category']
        model = Subcategory


class SubcategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'status', 'category']
        model = Subcategory
