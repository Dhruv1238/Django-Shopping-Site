from django.shortcuts import render
from .models import product
from math import ceil


# Create your views here.
def index(request):
    products= product.objects.all()
    print(products)
    n=len(products)
    nslides= n//4 + ceil((n/4)-(n//4))
    params={'no-of-slides':nslides,'range':range(1,nslides),'product': products}
    return render(request, 'shop/index.html', params)