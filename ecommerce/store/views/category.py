from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from ecommerce.store.models.category import Category
from ecommerce.store.serializers.category import (
    CategoryDetailSerializer,
    CategoryListSerializer,
)

swagger_attr = {'tags': ['Categories']}


class CategoryListApiView(ListAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        categories = Category.objects.all()
        return categories

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Listagem de todas as categorias',
        operation_description='Listagem de todas as categorias disponíveis',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryDetailApiView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        category = Category.objects.get(id=self.kwargs['pk'])
        return category

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Detalhes da categoria',
        operation_description='Detalhes da categoria selecionada',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
