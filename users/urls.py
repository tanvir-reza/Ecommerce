from django.urls import path,include
from .views import *

urlpatterns = [
    path('', signup_view, name='login'),
    # path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('success/', userSuccess,),
]
