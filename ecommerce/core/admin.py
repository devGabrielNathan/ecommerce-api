from django.contrib import admin

from .models import Address, Phone


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    ...


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    ...
