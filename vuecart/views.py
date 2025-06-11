from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


# Create your homepage views here.
def home(request):
    products=Product.objects.all().filter(is_available=True)
    context={
        'products': products
    }
    
    p = Product.objects.first()
    print(p.image)         # shows path or empty
    print(p.image.url)
    return render(request, 'home.html', context)