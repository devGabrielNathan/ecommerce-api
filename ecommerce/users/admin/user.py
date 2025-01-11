from django.contrib import admin
from django.contrib.auth import get_user_model

from ecommerce.users.admin.address import AddressInline
from ecommerce.users.admin.phone import PhoneInline

User = get_user_model()


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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
    ordering = ('email',)
    search_fields = (
        'username',
        'email',
    )
    inlines = [AddressInline, PhoneInline]
    list_max_show_all = 100
