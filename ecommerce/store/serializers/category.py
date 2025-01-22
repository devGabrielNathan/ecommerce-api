from rest_framework import serializers

from ecommerce.store.models.category import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'status']
        model = Category


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'status']
        model = Category
