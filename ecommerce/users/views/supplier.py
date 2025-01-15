from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from ecommerce.users.models.supplier import Supplier
from ecommerce.users.serializers.supplier import SupplierSerializer


# Create your views here.
class SupplierGenericListCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = (IsAdminUser,)
    queryset = Supplier.objects.all()


class SupplierGenericRetrieveUpdateDestroy(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = SupplierSerializer
    permission_classes = (IsAdminUser,)
    queryset = Supplier.objects.all()
