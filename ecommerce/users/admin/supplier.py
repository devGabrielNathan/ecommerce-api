from django.contrib import admin

from ecommerce.users.admin.address import AddressInline
from ecommerce.users.admin.phone import PhoneInline
from ecommerce.users.models.supplier import Supplier


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = (
        'email',
        'username',
        'is_active',
    )
    list_filter = ('is_active',)
    list_display = (
        'username',
        'email',
        'is_active',
    )
    ordering = ('email',)
    search_fields = (
        'username',
        'email',
    )
    inlines = [AddressInline, PhoneInline]
    list_max_show_all = 100
