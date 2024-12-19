from rest_framework import viewsets
from django.contrib.auth import get_user_model
from ecommerce.users import serializers

User = get_user_model()

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
