from django.contrib import admin

from .models import SupplierAddress, SupplierPhone, UserAddress, UserPhone


# Register your models here.
@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
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


class UserAddressInline(admin.TabularInline):
    model = UserAddress


@admin.register(SupplierAddress)
class SupplierAddressAdmin(admin.ModelAdmin):
    ...


class SupplierAddressInline(admin.TabularInline):
    model = SupplierAddress


@admin.register(UserPhone)
class UserPhoneAdmin(admin.ModelAdmin):
    ...


class UserPhoneInline(admin.TabularInline):
    model = UserPhone


@admin.register(SupplierPhone)
class SupplierPhoneAdmin(admin.ModelAdmin):
    ...


class SupplierPhoneInline(admin.TabularInline):
    model = SupplierPhone
