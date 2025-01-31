from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from ecommerce.orders.models.order import Order
from ecommerce.orders.serializers.order import (
    OrderDetailSerializer,
    OrderListCreateSerializer,
)

swagger_attr = {'tags': ['Orders']}


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderListCreateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.request.user
        cart_id = self.request.headers.get('Cart_ID')

        if user.is_authenticated:
            cart, _ = Order.objects.get_or_create(user=user)

        elif cart_id:
            cart, _ = Order.objects.get_or_create(id=cart_id)

        else:
            cart = Order.objects.none()

        return cart

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Listagem de todos os pedidos',
        operation_description='Listagem de todos os pedidos do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Criação de pedido',
        operation_description='Criação de pedido para o usuário logado',
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
        operation_summary='Detalhes do pedido',
        operation_description='Detalhes do pedido do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
