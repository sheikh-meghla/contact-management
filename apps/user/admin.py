from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import CustomUser 
from .models import profile    

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):

    list_display = ('email', 'is_staff', 'is_active', 'date_joined')

@admin.register(profile)
class ProfileAdmin(ModelAdmin):

    list_display = ('user', 'first_name', 'last_name')

# Register your models here.
