from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
# Create your views here.

def cart_summery(request):
    return render(request, 'cart/cart-summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == "POST":
        print("oky")
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity=product_quantity)
        
        response = JsonResponse({"Prodct Name":product.name,"product Qantity":product_quantity})
        return response
    



def cart_update():
    pass

def cart_delete():
    pass