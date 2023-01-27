from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.index, name="ShopHome"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('api', views.apitesting, name="apitesting"),
]