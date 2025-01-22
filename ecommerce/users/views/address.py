from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from ecommerce.users.models.address import Address
from ecommerce.users.serializers.address import (
    AddressDetailSerializer,
    AddressListCreateSerializer,
)

User = get_user_model()


class AddressListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressListCreateSerializer

    def get_queryset(self):
        addresses = Address.objects.filter(user=self.request.user)
        return addresses


class AddressDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressDetailSerializer

    def get_object(self):
        address = Address.objects.get(id=self.kwargs['pk'])
        return address
