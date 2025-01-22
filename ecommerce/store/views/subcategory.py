from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import AllowAny

from ecommerce.store.models.subcategory import Subcategory
from ecommerce.store.serializers.subcategory import (
    SubcategoryDetailSerializer,
    SubcategoryListSerializer,
)


class SubcategoryListApiView(ListAPIView):
    serializer_class = SubcategoryListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        subcategories = Subcategory.objects.all()
        return subcategories


class SubcategoryDetailApiView(RetrieveAPIView):
    serializer_class = SubcategoryDetailSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        subcategory = Subcategory.objects.get(id=self.kwargs['pk'])
        return subcategory
