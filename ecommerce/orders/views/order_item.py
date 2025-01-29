from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework.permissions import AllowAny

from ecommerce.orders.models.order_item import OrderItem
from ecommerce.orders.serializers.order_item import (
    OrderItemListCreateSerializer,
)


class OrderItemListCreateApiView(ListCreateAPIView):
    serializer_class = OrderItemListCreateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        order_item = OrderItem.objects.all()

        return order_item
