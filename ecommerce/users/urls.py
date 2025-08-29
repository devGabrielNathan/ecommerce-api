from django.urls import path

from ecommerce.users.views.address import (
    AddressDetailApiView,
    AddressListCreateApiView,
)
from ecommerce.users.views.phone import (
    PhoneDetailApiView,
    PhoneListCreateApiView,
)
from ecommerce.users.views.profile import ProfileGenericAPIView
from ecommerce.users.views.user import (
    ResetPasswordApiView,
    UserCreateAccountApiView,
    UserDetailApiView,
    UserLoginApiView,
    UserLogoutApiView,
)


urlpatterns = [
    path('register/', UserCreateAccountApiView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailApiView.as_view(), name='user-detail'),
    path('auth/login/', UserLoginApiView.as_view(), name='login'),
    path('auth/logout/', UserLogoutApiView.as_view(), name='logout'),
    path('profile/', ProfileGenericAPIView.as_view(), name='profile'),
    path(
        'password-reset/<uuid:pk>/',
        ResetPasswordApiView.as_view(),
        name='password-reset',
    ),
    path(
        'addresses/', AddressListCreateApiView.as_view(), name='address-list'
    ),
    path(
        'addresses/<uuid:pk>/',
        AddressDetailApiView.as_view(),
        name='address-detail',
    ),
    path('phones/', PhoneListCreateApiView.as_view(), name='phone-list'),
    path(
        'phones/<uuid:pk>/',
        PhoneDetailApiView.as_view(),
        name='phone-detail',
    ),
]
