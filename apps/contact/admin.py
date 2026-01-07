from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from apps.contact.models import Contact
@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'phone', 'user', 'profile_image')
