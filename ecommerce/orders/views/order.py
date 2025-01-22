from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from ecommerce.orders.serializers.order import OrderListCreateSerializer, OrderDetailSerializer
from ecommerce.orders.models.order import Order

from django.core.cache import cache

class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderListCreateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user)

        else:
            session_key = self.request.session.session_key
            if not session_key:
                self.request.session.create()
                session_key = self.request.session.session_key

            order_ids = cache.get(f'orders_{session_key}', [])

            return Order.objects.filter(id__in=order_ids)

class OrderDetailApiView(RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
