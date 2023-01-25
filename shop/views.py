from django.shortcuts import render
from .models import product
from math import ceil


# Create your views here.
def index(request):
    products= product.objects.all()
    print(products)
    n=len(products)
    ncards= n
    print(ncards)
    params={'no-of-cards':ncards,'range':range(1,ncards),'product': products}
    return render(request, 'shop/index.html', params)