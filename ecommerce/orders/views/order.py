from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from ecommerce.orders.models.order import Order
from ecommerce.orders.serializers.order import (
    OrderDetailSerializer,
    OrderListCreateSerializer,
)

swagger_attr = {'tags': ['Orders']}


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderListCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

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


class OrderDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Detalhes do pedido',
        operation_description='Detalhes do pedido do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Atualização do pedido',
        operation_description='Atualização do pedido do usuário logado',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
