from django.contrib import admin
from .models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'username', 'password')
    fields = ('name', 'url', 'username', 'password')
    search_fields = ('name', 'url', 'username', 'password')
