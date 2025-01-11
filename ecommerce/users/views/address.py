from rest_framework import generics

from ecommerce.users.models.address import Address
from ecommerce.users.serializers.address import AddressSerializer


class AddressGenericListCreate(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressGenericRetrieveUpdateDestroy(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
