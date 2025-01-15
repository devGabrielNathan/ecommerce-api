from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ecommerce.users.models.address import Address
from ecommerce.users.serializers.address import AddressSerializer


class AddressGenericListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressGenericRetrieveUpdateDestroy(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
