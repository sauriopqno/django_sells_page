from django.http import HttpResponse
from django.shortcuts import render
from products.models import product
from posts.models import Post

def homepage(request):
    products=product.objects.all().order_by('-date')
    posts=Post.objects.all().order_by('-time')
    context={
        'products':products,
         'posts':posts
    }
    return render(request, 'homepage.html',context)
    
def acerca_de(request):
    return render(request, 'acerca_de.html')
   