from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ecommerce.users.models.phone import Phone
from ecommerce.users.serializers.phone import PhoneSerializer


class PhoneGenericListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneGenericRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
