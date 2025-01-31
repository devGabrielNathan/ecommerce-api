from django.urls import path

from ecommerce.orders.views.order import (
    OrderDetailApiView,
    OrderListCreateAPIView,
)

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list'),
    path(
        'orders/<uuid:pk>/',
        OrderDetailApiView.as_view(),
        name='order-list',
    ),
]
