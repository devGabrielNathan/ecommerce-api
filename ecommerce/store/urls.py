from django.urls import path

from ecommerce.store.views.category import (
    CategoryDetailApiView,
    CategoryListApiView,
)
from ecommerce.store.views.subcategory import (
    SubcategoryDetailApiView,
    SubcategoryListApiView,
)

from ecommerce.store.views.product import (
    ProductDetailApiView,
    ProductListApiView,
)
urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='category-list'),
    path(
        'categories/<uuid:pk>/',
        CategoryDetailApiView.as_view(),
        name='category-detail',
    ),
    path(
        'subcategories/',
        SubcategoryListApiView.as_view(),
        name='subcategory-list',
    ),
    path(
        'subcategories/<uuid:pk>/',
        SubcategoryDetailApiView.as_view(),
        name='subcategory-detail',
    ),
    path(
        'products/',
        ProductListApiView.as_view(),
        name='product-list',
    ),
    path(
        'products/<uuid:pk>/',
        ProductDetailApiView.as_view(),
        name='product-detail',
    ),
]
