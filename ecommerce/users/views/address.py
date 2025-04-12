from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from ecommerce.users.models.address import Address
from ecommerce.users.serializers.address import (
    AddressDetailSerializer,
    AddressListCreateSerializer,
)

User = get_user_model()

swagger_attr = {'tags': ['Addresses']}


# Create your views here.
class AddressListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = AddressListCreateSerializer

    def get_queryset(self):
        addresses = Address.objects.filter(user=self.request.user)
        return addresses

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Listagem de todos os endereços',
        operation_description='Listagem de todos os endereços do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Criação de endereço',
        operation_description='Criação de endereço para o usuário logado',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AddressDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = AddressDetailSerializer

    def get_object(self):
        address = Address.objects.get(id=self.kwargs['pk'])

        if address.user != self.request.user:
            raise PermissionDenied(
                'Você não tem permissão para acessar este endereço.'
            )
        return address

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Detalhes do endereço',
        operation_description='Detalhes do endereço do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Atualização das informações de endereço',
        operation_description='Atualização das informações de endereço do usuário logado',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Remoção de endereço',
        operation_description='Remoção de endereço do usuário logado',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
