from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


# Create your homepage views here.
def home(request):
    products=Product.objects.all().filter(is_available=True)
    
    context={
        'products': products
    }
    print(context,"abinesh")
    return render(request, 'home.html', context)