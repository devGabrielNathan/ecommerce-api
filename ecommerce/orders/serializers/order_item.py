from rest_framework import serializers

from ecommerce.orders.models.order_item import OrderItem
from ecommerce.store.models.product import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), required=True
    )

    class Meta:
        fields = ['id', 'product', 'quantity', 'subtotal']
        model = OrderItem
        read_only_fields = ['id', 'subtotal']
