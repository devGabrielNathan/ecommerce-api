from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from ecommerce.users.serializers.user import (
    ResetPasswordSerializer,
    UserCreateAccountSerializer,
    UserDetailSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
)

User = get_user_model()

swagger_attr = {'tags': ['Users']}


# Create your views here.
class UserCreateAccountApiView(CreateAPIView):
    serializer_class = UserCreateAccountSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Criação de conta de usuário',
        operation_description='Criação de conta de usuário com nome, email e senha.',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user = User.objects.get(id=self.kwargs['pk'])
        return user

    def get_queryset(self):
        users = User.objects.all()
        return users

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Detalhes do usuário',
        operation_description='Detalhes do usuário logado.',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Atualização das informações do usuário',
        operation_description='Atualização das informações do usuário logado.',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Remoção do usuário',
        operation_description='Remoção do usuário logado.',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UserLoginApiView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Login do usuário',
        operation_description='Efetua o login do usuário',
        request_body=serializer_class,
    )
    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class UserLogoutApiView(APIView):
    serializer_class = UserLogoutSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Logout do usuário',
        operation_description='Efetua o Logout do usuário.',
        request_body=serializer_class,
    )
    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED
            )


class ResetPasswordApiView(UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user = User.objects.get(id=self.kwargs['pk'])
        return user

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Reset de senha',
        operation_description='Reset de senha do usuário logado.',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
