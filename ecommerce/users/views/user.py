from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ecommerce.users.serializers.user import (
    UserLoginSerializer,
    UserLogoutSerializer,
    UserSerializer,
)



User = get_user_model()


# Create your views here.
class UserAccess(
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericAPIView,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request) -> Response:
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginObtainPairView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            validated_data = serializer.validated_data
            id = validated_data.get('id')
            user = User.objects.get(id=id)
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            response = {
                'id': str(id),
                'refresh': str(refresh),
                'access': str(access),
            }

            return Response(
                data=response, status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
# class UserLoginObtainPairView(APIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
        
#         if serializer.is_valid():
#             validated_data = serializer.validated_data
#             id = validated_data.get('id')
#             user = User.objects.get(id=id)
#             refresh = RefreshToken.for_user(user)
#             access = refresh.access_token

#             response = {
#                 'id': str(id),
#                 'refresh': str(refresh),
#                 'access': str(access),
#             }

#             return Response(
#                 data=response, status=status.HTTP_200_OK
#             )
#         else:
#             return Response(
#                 data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
#             )



class UserLogoutApiView(APIView):
    serializer_class = UserLogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            refresh_token = RefreshToken(validated_data['refresh'])
            refresh_token.blacklist()

            return Response(
                data=refresh_token, status=status.HTTP_205_RESET_CONTENT
            )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED
            )
