from django.contrib import admin

from ecommerce.users.models.phone import Phone


# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    fields = (
        'DDD',
        'number',
        'user',
        'supplier',
    )
    list_filter = ('DDD',)
    list_display = (
        'DDD',
        'number',
        'user',
        'supplier',
    )
    ordering = ('DDD',)
    search_fields = (
        'number',
        'user',
        'supplier',
    )


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1
