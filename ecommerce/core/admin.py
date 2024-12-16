from django.contrib import admin

from .models import Address, Phone


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    ...


class AddressInline(admin.TabularInline):
    model = Address


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    ...


class PhoneInline(admin.TabularInline):
    model = Phone
