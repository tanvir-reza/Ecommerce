from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True,null=True)
    # address = models.CharField(max_length=200)
    # city = models.CharField(max_length=50)
    # country = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='profile/', default='profile/user-default.png')

    def __str__(self):
        return self.name
    
