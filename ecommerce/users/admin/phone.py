from django.contrib import admin

from ecommerce.users.models.phone import Phone


# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    fields = (
        'DDD',
        'number',
        'user',
    )
    list_filter = ('DDD',)
    list_display = (
        'DDD',
        'number',
        'user',
    )
    ordering = ('DDD',)
    search_fields = (
        'number',
        'user',
    )


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1
