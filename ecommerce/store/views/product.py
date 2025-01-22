from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from ecommerce.store.serializers.product import ProductListSerializer, ProductDetailSerializer
from ecommerce.store.models.product import Product

class ProductListApiView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Product.objects.all()
    

class ProductDetailApiView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)
    
    def get_object(self):
        product =  Product.objects.get(pk=self.kwargs['pk'])
        return product
