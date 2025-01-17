from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ecommerce.users.models.phone import Phone
from ecommerce.users.serializers.phone import (
    PhoneCreateSerializer,
    PhoneDetailSerializer,
)


class PhoneCreateApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhoneCreateSerializer


class PhoneDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhoneDetailSerializer

    def get_object(self):
        phone = Phone.objects.get(id=self.kwargs['pk'])
        return phone
