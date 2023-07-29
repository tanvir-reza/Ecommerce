from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'store/product_details.html', context)

def categoryProducts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    count = products.count()
    context = {
        'category': category,
        'products': products,
        'count': count
    }
    return render(request, 'store/list-category.html', context)

def categorys(request):
    all_category = Category.objects.all()
    return {'all_category': all_category}