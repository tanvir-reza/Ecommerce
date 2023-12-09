from django.urls import path,include
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [

    path('add-cart/', cart_add, name='add_to_cart'),
    path('cart-summery/', cart_summery, name='cart-summery'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('payment-status/', payment_status, name='payment_status'),
    path('pdf/', download_pdf, name='pdf'),
    # path('update/', cart_update, name='cart_update'),
    # path('delete', cart_delete, name='cart_delete'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)