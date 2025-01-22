from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from ecommerce.store.models.category import Category
from ecommerce.store.serializers.category import (
    CategoryDetailSerializer,
    CategoryListSerializer,
)


class CategoryListApiView(ListAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        categories = Category.objects.all()
        return categories


class CategoryDetailApiView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        category = Category.objects.get(id=self.kwargs['pk'])
        return category
