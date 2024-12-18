from rest_framework import viewsets
from ecommerce.core import models
from ecommerce.core import serializers

# Create your views here.
class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer
