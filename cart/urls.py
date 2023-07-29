from django.urls import path,include
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('', cart_summery, name='cart-summery'),
    path('add/', cart_add, name='cart-add'),
    path('update/', cart_update, name='cart_update'),
    path('delete', cart_delete, name='cart_delete'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)