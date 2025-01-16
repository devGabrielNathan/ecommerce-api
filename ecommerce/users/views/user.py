from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.users.serializers.user import (
    UserAccountSerializer,
    UserCreateAccountSerializer,
    ResetPasswordSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
)

User = get_user_model()


# Create your views here.
class UserCreateAccountApiView(CreateAPIView):
    serializer_class = UserCreateAccountSerializer
    permission_classes = (AllowAny,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
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

    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED
            )


class ResetPassword(UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
