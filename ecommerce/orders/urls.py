from ecommerce.orders.views.order import OrderListCreateAPIView, OrderDetailApiView

from ecommerce.orders.views.order_item import OrderItemListCreateApiView
from django.urls import path


urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list'),
    path('orders/<uuid:pk>/', OrderListCreateAPIView.as_view(), name='order-list'),
    # path('carts/',OrderItemListCreateApiView.as_view(), name='order-create'),
    # path('carts/<uuid:pk>/', OrderItemDetailApiView.as_view(), name='order-create'),
]
