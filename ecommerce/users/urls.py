from django.urls import path

from ecommerce.users.views.address import (
    AddressCreateApiView,
    AddressDetailApiView,
)
from ecommerce.users.views.phone import (
    PhoneCreateApiView,
    PhoneDetailApiView,
)
from ecommerce.users.views.user import (
    ResetPasswordApiView,
    UserCreateAccountApiView,
    UserDetailApiView,
    UserLoginApiView,
    UserLogoutApiView,
)

urlpatterns = [
    path('users/', UserCreateAccountApiView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailApiView.as_view(), name='user-detail'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path(
        'password-reset/<uuid:pk>/',
        ResetPasswordApiView.as_view(),
        name='password-reset',
    ),
    path('addresses/', AddressCreateApiView.as_view(), name='address-list'),
    path(
        'addresses/<uuid:pk>/',
        AddressDetailApiView.as_view(),
        name='address-detail',
    ),
    path('phones/', PhoneCreateApiView.as_view(), name='phone-list'),
    path(
        'phones/<uuid:pk>/',
        PhoneDetailApiView.as_view(),
        name='phone-detail',
    ),
]
