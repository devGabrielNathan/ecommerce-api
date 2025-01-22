from rest_framework import serializers

from ecommerce.store.models.subcategory import Subcategory


class SubcategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'status']
        model = Subcategory


class SubcategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'status']
        model = Subcategory
