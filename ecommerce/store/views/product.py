from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from ecommerce.store.models.product import Product
from ecommerce.store.serializers.product import (
    ProductDetailSerializer,
    ProductListSerializer,
)

swagger_attr = {'tags': ['Products']}


class ProductListApiView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Product.objects.all()

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Listagem de todos os produtos',
        operation_description='Listagem de todos os produtos',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailApiView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        return product

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Detalhes do produto',
        operation_description='Detalhes do produto',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
