from django.contrib import admin
from ecommerce.users.models.profile import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'bio',
        'avatar',
    )
    list_display = (
        'user',
        'bio',
    )
    ordering = ('user',)
    search_fields = (
        'user__username',
        'user__email',
    )

    list_max_show_all = 100