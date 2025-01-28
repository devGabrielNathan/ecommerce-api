from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ecommerce.orders.serializers.order_item import OrderItemListCreateSerializer, OrderItemDetailSerializer

from ecommerce.orders.models.order import Order
from ecommerce.orders.models.order_item import OrderItem


class OrderItemListCreateApiView(ListCreateAPIView):
    serializer_class = OrderItemListCreateSerializer
    permission_classes = (AllowAny,)


    def get_queryset(self):
        order_item = OrderItem.objects.all()

        return order_item
    
    
