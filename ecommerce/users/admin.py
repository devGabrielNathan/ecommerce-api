from django.contrib import admin

from ..core.admin import SupplierAddressInline, SupplierPhoneInline, UserAddressInline, UserPhoneInline
from .models import Supplier, User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Reorganizing the arrangement of fields in the administration panel and adding creation options for address and telephone dynamically.
    """
    fields = (
        'email',
        'username',
        'password',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_staff',
        'is_active',
    )
    list_display = (
        'email',
        'username',
        'is_staff',
        'is_active',
    )
    ordering = (
        'email',
    )
    search_fields = (
        'username',
        'email',
    )
    inlines = [
        UserAddressInline,
        UserPhoneInline
    ]
    list_max_show_all = 100


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = (
        'email',
        'username',
        'password',
        'is_active',
    )
    list_filter = (
        'is_active',
    )
    list_display = (
        'username',
        'email',
        'is_active',
    )
    ordering = (
        'email',
    )
    search_fields = (
        'username',
        'email',
    )
    inlines = [
        SupplierAddressInline,
        SupplierPhoneInline
    ]
    list_max_show_all = 100
