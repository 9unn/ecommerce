"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('home/', views.Home, name='Home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('home/', views.Home, name='Home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from .views import ProductsView, ProductDetailView


app_name = 'myapp'

urlpatterns = [

    path('', views.Home, name='Home'),
    # path('bestseller/', views.bestseller, name='bestseller'),
    # path('new/', views.new, name='new'),
    path('product-detail/', ProductDetailView.as_view(), name='productdetail'),
    # path('product-detail/<id>/', ProductDetailView.as_view(), name='productdetail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('products/', ProductsView.as_view(), name='products'),
    path('products/<slug>', views.Product, name='products'),

    path('about/', views.about, name='about'),

    path('acc/', views.account, name='account'),
    path('register/', views.reg, name='Reg'),
    path('login/', views.login, name='Login'),


    path('order/', views.Order, name='order'),
    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('address', views.address,name='address'),



    

    # path('orderplace/', views.)
    # path('top/', views.top, name='top'),


]