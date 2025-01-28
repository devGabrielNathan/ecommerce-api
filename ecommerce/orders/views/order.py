from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from ecommerce.orders.serializers.order import OrderListCreateSerializer, OrderDetailSerializer
from ecommerce.orders.models.order import Order

from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema

swagger_attr = {
    "tags": ["Orders"]
}

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

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary="Listagem de todos os pedidos",
        operation_description="Listagem de todos os pedidos do usuário logado",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        **swagger_attr,
        operation_summary="Criação de pedido",
        operation_description="Criação de pedido para o usuário logado",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class OrderDetailApiView(RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary="Detalhes do pedido",
        operation_description="Detalhes do pedido do usuário logado",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
