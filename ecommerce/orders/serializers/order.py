from django.contrib.auth import get_user_model
from rest_framework import serializers

from ecommerce.orders.models.order import Order
from ecommerce.orders.models.order_item import OrderItem
from ecommerce.orders.serializers.order_item import OrderItemSerializer

User = get_user_model()


class OrderListCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            if quantity > product.quantity:
                if product.status == 'inactive':
                    raise serializers.ValidationError(
                        f'O produto {product.name} está inativo.'
                    )
                raise serializers.ValidationError(
                    f'A quantidade solicitada para {product.name} excede o estoque disponível ({product.quantity}).'
                )

            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
            )

            product.quantity -= quantity
            product.save()

            order_item.subtotal = product.price * quantity
            order_item.save()

        return order


class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    items = OrderItemSerializer(many=True)

    class Meta:
        fields = ['id', 'user', 'items']

        model = Order
        read_only_fields = ['id', 'user']
        required_fields = ['items']
