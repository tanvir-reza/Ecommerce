from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=False,null=True)
    email = models.EmailField(max_length=255, blank=False, null=True)
    name = models.CharField(max_length=255, blank=False, null=False,default='')
    phone = models.CharField(max_length=20, blank=False, null=False,default='')
    Shipping_address = models.CharField(max_length=255, blank=False, default='Dhaka')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
    
    