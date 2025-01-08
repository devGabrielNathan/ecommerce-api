from django.contrib.auth import authenticate, get_user_model, login
from rest_framework import status, views, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ecommerce.users import serializers

User = get_user_model()


# Create your views here.
class UserModelViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('password2', None)
            password = validated_data.pop('password1')
            user = User.objects.create_user(
                password=password, **validated_data
            )
            user.save()

            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginViewSet(views.APIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                login(request, user)

                return Response(
                    {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {'error': 'Invalid credentials.'},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
