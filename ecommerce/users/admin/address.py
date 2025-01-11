from django.contrib import admin

from ecommerce.users.models.address import Address


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
        'cep',
        'user',
        'supplier',
    )
    list_filter = (
        'state',
        'neighborhood',
    )
    list_display = (
        'state',
        'city',
        'neighborhood',
        'street',
        'number',
        'complement',
        'cep',
    )
    ordering = ('state',)
    search_fields = (
        'username',
        'email',
    )

    list_max_show_all = 100


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
