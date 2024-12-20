from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.response import Response

from ecommerce.users import serializers

User = get_user_model()

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('password2', None)
            password = validated_data.pop('password1')
            user = User.objects.create_user(password=password, **validated_data)
            user.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
