from django.db import models
from apps.user.models import CustomUser

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to='contact_images/', blank=True, null=True)
    def __str__(self):
        return self.name