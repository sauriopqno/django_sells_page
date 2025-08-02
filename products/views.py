from django.shortcuts import render
from .models import product

def product_lists(request):
    products=product.objects.all().order_by('-date')
    return render(request, "products/products.html",{'products':products})

def product_page(request, slug):
    producto=product.objects.get(slug=slug)
    return render(request, "products/product_page.html",{'product':producto})


# Create your views here.
