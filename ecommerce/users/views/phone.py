from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from ecommerce.users.models.phone import Phone
from ecommerce.users.serializers.phone import (
    PhoneDetailSerializer,
    PhoneListCreateSerializer,
)


class PhoneListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhoneListCreateSerializer

    def get_queryset(self):
        phones = Phone.objects.filter(user=self.request.user)
        return phones


class PhoneDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhoneDetailSerializer

    def get_object(self):
        phone = Phone.objects.get(id=self.kwargs['pk'])
        return phone
