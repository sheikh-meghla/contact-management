from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Contact 
   

@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    

    list_display = ('mobile_ower_name','name','phone_number', 'date_created')

    def mobile_ower_name(self, obj):
        return obj.user.profile.first_name + " " + obj.user.profile.last_name

