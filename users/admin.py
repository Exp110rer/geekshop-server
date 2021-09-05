from django.contrib import admin
from users.models import User


# Register your models here.

# admin.site.register(User)

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username',)
    fields = (('first_name', 'last_name'), 'username', ('is_staff', 'is_active'),)
    readonly_fields = ('is_active', 'is_staff', 'username',)
    ordering = ('-last_name',)
    search_fields = ('last_name',)
