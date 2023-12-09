from django.db.models.signals import post_save,post_init
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.conf import settings

@receiver(user_signed_up)
def createProfile(request,user, **kwargs):
    print("profile Trigger")
    profile = Profile.objects.create(
        user = request.user,
        name = "User",
    )

