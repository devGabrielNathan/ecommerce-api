from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from ecommerce.users.models.address import Address
from ecommerce.users.serializers.address import (
    AddressCreateSerializer,
    AddressDetailSerializer,
)


class AddressCreateApiView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AddressCreateSerializer


class AddressDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressDetailSerializer

    def get_object(self):
        address = Address.objects.get(id=self.kwargs['pk'])
        return address
