from django.contrib.auth import get_user_model
from rest_framework import serializers

from ecommerce.orders.models.order import Order
from ecommerce.orders.models.order_item import OrderItem
from ecommerce.orders.serializers.order_item import OrderItemSerializer

User = get_user_model()


class OrderListCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
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
            list_of_items = OrderItem.objects.create(
                order=order,
                product=item_data['product'],
                quantity=item_data['quantity'],
            )
            order.order_item.add(list_of_items.product)

        return order


class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )
    items = OrderItemSerializer(many=True)

    class Meta:
        fields = ['id', 'user', 'items']

        model = Order


# # Não preciso de uma view para esse cara
# pedido_produto = {
#     'pedido': 'Teste',
#     'produto': 'Computador',
#     'quantidade': 1,
# }

# # Só para esse
# pedido = {
#     'nome': 'Teste',
#     'items': [pedido_produto],
# }

# # E para esse
# produto = {
#     'nome': 'Computador',
# }
