from rest_framework import serializers

from ecommerce.store.models.subcategory import Subcategory
from ecommerce.store.models.category import Category


class SubcategoryListSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=True
    )

    class Meta:
        fields = ['id', 'name', 'status', 'category']
        model = Subcategory


class SubcategoryDetailSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=True
    )

    class Meta:
        fields = ['id', 'name', 'status', 'category']
        model = Subcategory
