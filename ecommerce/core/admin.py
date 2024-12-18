from django.contrib import admin

from .models import Address, Phone


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = (
        'state',
        'city',
        'neighborhood',
        'street',
        'number',
        'complement',
        'cep'
    )
    list_filter = (
        'state',
        'neighborhood',
    )
    # list_display = (
    #     'username',
    #     'email',
    #     'is_staff',
    #     'is_active',
    # )
    # ordering = (
    #     'email',
    # )
    # search_fields = (
    #     'username',
    #     'email',
    # )

    list_max_show_all = 100
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    ...


class AddressInline(admin.TabularInline):
    model = Address


class PhoneInline(admin.TabularInline):
    model = Phone
