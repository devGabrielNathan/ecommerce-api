"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ecommerce.core.viewsets import AddressViewSet, PhoneViewSet
from ecommerce.users.viewsets import UserViewSet

router = DefaultRouter()
router.register(r'phones', PhoneViewSet, basename='phone')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [path('admin/', admin.site.urls), path('', include(router.urls))]
