from django.contrib import admin

from .models import Auth

@admin.register(Auth)
class AuthAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'name', 'lastname', 'is_active', 'is_staff', 'is_superuser', 'is_superadmin')
    search_fields = ('email', 'username', 'name', 'lastname')
    list_filter = ('is_active', 'is_staff', 'is_superadmin')
    ordering = ('email',)