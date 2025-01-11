from rest_framework import generics

from ecommerce.users.models.phone import Phone
from ecommerce.users.serializers.phone import PhoneSerializer


class PhoneGenericListCreate(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneGenericRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
