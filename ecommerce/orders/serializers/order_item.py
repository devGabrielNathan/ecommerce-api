from rest_framework import serializers

from ecommerce.orders.models.order import Order
from ecommerce.orders.models.order_item import OrderItem
from ecommerce.store.models.product import Product


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), required=False
    )
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), required=True
    )

    class Meta:
        fields = ['id', 'order', 'product', 'quantity']
        model = OrderItem
