from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email',)
    
