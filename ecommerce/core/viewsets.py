from rest_framework import viewsets

from ecommerce.core.models import Address, Phone
from ecommerce.core.serializers import AddressSerializer, PhoneSerializer


# Create your views here.
class AddressModelViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
