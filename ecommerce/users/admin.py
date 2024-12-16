from django.contrib import admin

from ..core.admin import AddressInline, PhoneInline
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Reorganizing the arrangement of fields in the administration panel and adding creation options for address and telephone dynamically.
    """
    fields = (
        'username',
        'email',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_staff',
        'is_active',
    )
    list_display = (
        'username',
        'email',
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
        AddressInline,
        PhoneInline
    ]
    list_max_show_all = 100
