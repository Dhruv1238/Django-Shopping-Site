from django.shortcuts import render, HttpResponse, redirect
from .models import product
from math import ceil
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import requests

# Create your views here.
def index(request):
    products= product.objects.all()
    print(products)
    n=len(products)
    ncards= n
    print(ncards)
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=1r39OfmHy15xyesTuzvrMFaZvXaDaUIz2CXHcgua").json()
    params={'no-of-cards':ncards,'range':range(1,ncards),'product': products, 'response':response}
    return render(request, 'shop/index.html', params)

def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        pass1=request.POST['pass1']
        
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters")
            return redirect('ShopHome')
        
        myuser = User.objects.create_user(username, email, pass1)  
        myuser.save()
        messages.success(request, "Account created successfully")
        return redirect('ShopHome')
    else:
        return HttpResponse('Badmashi')
    
def handlelogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        
        user= authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('ShopHome')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('ShopHome')
    return HttpResponse("Badmashi")
    
def handlelogout(request):
    logout(request)
    messages.success(request, "loggedout")
    return redirect('ShopHome')

    

def apitesting(request):
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=1r39OfmHy15xyesTuzvrMFaZvXaDaUIz2CXHcgua").json()
    # return HttpResponse(response)
    return render(request, "shop/api.html", {'response':response})