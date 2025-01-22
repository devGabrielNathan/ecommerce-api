from rest_framework import serializers

from ecommerce.orders.models.order import Order

from django.contrib.auth import get_user_model

from django.core.cache import cache

User = get_user_model()


class OrderListCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        fields = [
            'id',
            'user'
        ]

        model = Order

    def create(self, validated_data):
        user = self.context['request'].user
        request = self.context['request']
        
        if user.is_authenticated:
            order = Order.objects.create(user=user, **validated_data)
        else:
            order = Order.objects.create(**validated_data)
            session_key = request.session.session_key

            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            orders = cache.get(f'orders_{session_key}', [])
            orders.append(order.id)
            cache.set(f'orders_{session_key}', orders, timeout=60 * 60 * 24)
        
        return order

class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        fields = [
            'id',
            'user'
        ]

        model = Order
