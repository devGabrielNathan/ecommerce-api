from django.urls import path

from ecommerce.users.views.address import (
    AddressGenericListCreate,
    AddressGenericRetrieveUpdateDestroy,
)
from ecommerce.users.views.phone import (
    PhoneGenericListCreate,
    PhoneGenericRetrieveUpdateDestroy,
)
from ecommerce.users.views.supplier import (
    SupplierGenericListCreate,
    SupplierGenericRetrieveUpdateDestroy,
)
from ecommerce.users.views.user import (
    UserPublicAccess,
    ResetPassword,
    UserDetail,
    UserLoginView,
    UserLogoutApiView,
)

urlpatterns = [
    path('users/', UserPublicAccess.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetail.as_view(), name='user-detail'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('password-reset/<uuid:pk>/', ResetPassword.as_view(), name='password-reset'),
    path(
        'suppliers/', SupplierGenericListCreate.as_view(), name='supplier-list'
    ),
    path(
        'suppliers/<uuid:pk>/',
        SupplierGenericRetrieveUpdateDestroy.as_view(),
        name='supplier-detail',
    ),
    path(
        'addresses/', AddressGenericListCreate.as_view(), name='address-list'
    ),
    path(
        'addresses/<uuid:pk>/',
        AddressGenericRetrieveUpdateDestroy.as_view(),
        name='address-detail',
    ),
    path('phones/', PhoneGenericListCreate.as_view(), name='phone-list'),
    path(
        'phones/<uuid:pk>/',
        PhoneGenericRetrieveUpdateDestroy.as_view(),
        name='phone-detail',
    ),
]
