from django.contrib import admin

# Register your models here.
from apps.contact.models import Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'user', 'profile_image')
