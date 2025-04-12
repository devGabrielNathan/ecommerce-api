from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from ecommerce.users.models.phone import Phone
from ecommerce.users.serializers.phone import (
    PhoneDetailSerializer,
    PhoneListCreateSerializer,
)

swagger_attr = {'tags': ['Phones']}


class PhoneListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PhoneListCreateSerializer

    def get_queryset(self):
        phones = Phone.objects.filter(user=self.request.user)
        return phones

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Listagem de todos os telefones',
        operation_description='Listagem de todos os telefones do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Criação de telefone',
        operation_description='Criação de telefone para o usuário logado',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PhoneDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PhoneDetailSerializer

    def get_object(self):
        phone = Phone.objects.get(id=self.kwargs['pk'])
        if phone.user != self.request.user:
            raise PermissionDenied(
                'Você não tem permissão para acessar este telefone.'
            )
        return phone

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Detalhes do telefone',
        operation_description='Detalhes do telefone do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Atualização de telefone',
        operation_description='Atualização de telefone do usuário logado',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Remoção de telefone',
        operation_description='Remoção de telefone do usuário logado',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
