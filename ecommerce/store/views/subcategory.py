from drf_yasg.utils import swagger_auto_schema
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

swagger_attr = {'tags': ['Subcategories']}


# Create your views here.
class SubcategoryListApiView(ListAPIView):
    serializer_class = SubcategoryListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        subcategories = Subcategory.objects.all()
        return subcategories

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Listagem de todas as subcategorias',
        operation_description='Listagem de todas as subcategorias',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SubcategoryDetailApiView(RetrieveAPIView):
    serializer_class = SubcategoryDetailSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        subcategory = Subcategory.objects.get(id=self.kwargs['pk'])
        return subcategory

    def get_queryset(self):
        subcategories = Subcategory.objects.all()
        return subcategories

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Detalhes da subcategoria',
        operation_description='Detalhes da subcategoria',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
