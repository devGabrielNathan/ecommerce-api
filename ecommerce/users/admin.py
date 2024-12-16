from django.contrib import admin

from .models import User
from ..core.admin import AddressInline
from ..core.admin import PhoneInline


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
        PhoneInline
    ]
