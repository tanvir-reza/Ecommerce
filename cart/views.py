from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.core import cache
from store.models import Product
from django.http import HttpResponse

from django.shortcuts import get_object_or_404,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def cart_add(request):
    # cache.clear()
    if request.method == 'POST':
        
        product_id = request.POST.get('prod_id')
        qunatity = int(request.POST.get('qty'))
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += qunatity
        else:
            cart[product_id] = qunatity
        request.session['cart'] = cart
        length = len(cart)
        print(cart)
        return JsonResponse({'length':length})
        


def cart_summery(request):
    cart = request.session.get('cart', {})
    product_price = 0
    cart_items = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product_price += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity})
    length = len(cart_items)
    print(product_price)
    return render(request, 'cart/cart-summary.html', {'cart_items': cart_items,'product_price':product_price})


def checkout(request):
    cart = request.session.get('cart', {})
    product_price = 0
    cart_items = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product_price += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity})

    return render(request, 'cart/checkout.html',{'cart_items': cart_items,'product_price':product_price})

def payment(request):

    if request.method == 'POST':
        success = 'http://127.0.0.1:8000/cart/payment-status/'
        if request.POST.get('payment') == 'ssl':
            from sslcommerz_lib import SSLCOMMERZ 
            settings = { 'store_id': 'abc6574d69b71365', 'store_pass': 'abc6574d69b71365@ssl', 'issandbox': True }
            sslcz = SSLCOMMERZ(settings)
            post_body = {}
            post_body['total_amount'] = 100.26
            post_body['currency'] = "BDT"
            post_body['tran_id'] = "12345"
            post_body['success_url'] = success
            post_body['fail_url'] = "your fail url"
            post_body['cancel_url'] = "your cancel url"
            post_body['emi_option'] = 0
            post_body['cus_name'] = "test"
            post_body['cus_email'] = "test@test.com"
            post_body['cus_phone'] = "01700000000"
            post_body['cus_add1'] = "customer address"
            post_body['cus_city'] = "Dhaka"
            post_body['cus_country'] = "Bangladesh"
            post_body['shipping_method'] = "NO"
            post_body['multi_card_name'] = ""
            post_body['num_of_item'] = 1
            post_body['product_name'] = "Test"
            post_body['product_category'] = "Test Category"
            post_body['product_profile'] = "general"

            response = sslcz.createSession(post_body) # API response
            return redirect(response['GatewayPageURL'])
            print(response)
        
    return redirect('checkout')

@csrf_exempt
def payment_status(request):
    if request.method == 'POST':
        payment_data = request.POST
        print(payment_data)
        if payment_data['status'] == 'VALID':
            return HttpResponse('ok')
        return HttpResponse('ok')
    

def payment_success(request,val_id,tran_id):
    if request.method == 'POST':
        payment_data = request.POST
        print(payment_data)
        if payment_data['status'] == 'VALID':
            return HttpResponse('ok')
        return HttpResponse('ok')
    

# PDF GENERATOR
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
import os

def emni(request):
    return render(request,'cart/pdf.html')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    print(html)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result,encoding='ISO-8859-1')
    print(pdf)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def download_pdf(request):
    cart = request.session.get('cart', {})
    product_price = 0
    cart_items = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product_price += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity})
    
    context = {
        'cart_items': cart_items,
        'product_price':product_price
        
    }
    # Create a Django response object, and specify content_type as pdf
    template_path = 'cart/pdf.html'
    response = HttpResponse(content_type='application/pdf')
    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,encoding='ISO-8859-1')
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# class cart(generic.TemplateView):
#     template_name = "cart/cart-summary.html"

    

# class cart_add(generic.View):
    
#     def post(self,*args,**kwargs):
#         print("oky")
#         product = get_object_or_404(Product,id=kwargs.get('id'))
#         print("oky")
#         cart = Cart(self.request)
#         cart.update(product.id,1)
#         return redirect('store')



# def cart_update():
#     pass

# def cart_delete():
#     pass