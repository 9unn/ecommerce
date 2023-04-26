from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from . import forms,models
from .forms import LoginForm, RegForm, AddressForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Product


def login(request):
   if request.method == "POST": 
       LoginForm = LoginForm(request.POST) 
       LoginForm =forms.LoginForm(request.POST, request.FILES)
       if LoginForm.is_valid(): 
            
            print('Username:', LoginForm.cleaned_data['Username'])
            print('Password:',LoginForm.cleaned_data['Password'])
            
            return redirect('products')
   else: 
       LoginForm = LoginForm() 
       
   return render(request, "products.html", {'LoginForm':login})

def reg(request):
   if request.method == "POST": 
       RegForm = RegForm(request.POST) 
       RegForm =forms.RegForm(request.POST, request.FILES)
       if RegForm.is_valid(): 
            print('Username:', RegForm.cleaned_data['Username'])
            print('Email:', RegForm.cleaned_data['Email']) 
            print('Password:',RegForm.cleaned_data['Password'])
            
            return redirect('products')
   else: 
       form = RegForm() 

   return render(request, "products.html", {'RegForm':reg})

def Home(request):
    return render(request,'home.html', {'Home':Home})

def about(request):
    return render(request, "about.html", {'about':about})

def account(request):
    return render(request, "account.html", {'account':account})


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "productdetail.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = 'productdetail.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        # # fetch the object based on a different identifier, e.g. the product code
        # product_code = self.kwargs.get('id')
        # obj = get_object_or_404(queryset, id = product_code)
        # return obj

    def productdetail(request):
        productdetail = get_object_or_404(models.Product)
        if 'product_title' in request.COOKIES:            
            product_title = request.COOKIES['product_title']
            counter = product_title.split('|')
            product_count_in_cart = len(set(counter))
        else:
            product_count_in_cart = 0
            context = {
            'p': productdetail,
            'product_count_in_cart': product_count_in_cart,}
        return render(request, "productdetail.html",  {'productdetail':productdetail})


class ProductsView(ListView):
    model = Product
    template = 'products.html'

    def products(request):
        products = models.Product.objects.all()
        if 'product_title' in request.COOKIES:
            product_title = request.COOKIES['product_title']
            counter = product_title.split('|')
            product_count_in_cart=len(set(counter)) 

        else:
            product_count_in_cart = 0
            context = {
            'p': products,
            'product_count_in_cart': product_count_in_cart,}
        # if request.user.is_authenticated:
            return HttpResponseRedirect('products')
        return render(request,'products_list.html', {'product_count_in_cart':product_count_in_cart})


# def Order(request):
#     Order = models.Order.objects.all()
#     if 'order_ids' in request.COOKIES:
#         order_ids = request.COOKIES['order_ids']

#         products = None
#         total=0
#     
#         product_id_in_cart = products.split()
#    
#     if  request.user.is_authenticated
        #   product_id_in_cart = products.split()
#         products = models.Product.objects.all().filter(id__in = product_id_in_cart)
        
#         for p in products:
#             total = total + p.price
#     return render(request, "order.html", {'products':products,'total':total,'order':Order})

# def top(request):
#     top = models.top.objects.all()
#     if 'tops' in request.COOKIES:
#         tops = request.COOKIES['tops']

#     if request.user.is_authenticated:
#         return HttpResponseRedirect('top')
#     return render(request, "top.html", {'top':top})

# def logout(request):
#     return render(request, "logout.html", {'logout':logout})


def bestseller(request):
    bestseller = models.bestseller.object.all()
    if request.user.is_autheticated:
        return HttpResponseRedirect('bestseller')
    return render(request, "home.html", {'bestseller':bestseller})


def new(request):
    new = models.new.object.all()
    if 'new' in request.COOKIES:
        new = request.COOKIES['new']

    if request.user.is_autheticated:
        return HttpResponseRedirect('new')
    return render(request, "home.html", {'new':new})


def add_to_cart_view(request,pk):
    products = models.Product.objects.all()

    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        counter = product_title.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=1

    response = render(request, 'home.html',{'products':products,'product_count_in_cart':product_count_in_cart})
    # response = render(request, 'homepage.html',{'products':products,'product_count_in_cart':product_count_in_cart,'redirect_to' : request.GET['next_page']})

    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        if product_title =="":
            product_title = str(pk)
        else:
            product_title = str(product_title)+"|"+str(pk)
        response.set_cookie('product_title', product_title)
        
    else:
        product_title = pk
        response.set_cookie('product_title', pk)
  

    product = models.Product.objects.get(id=pk)
    messages.info(request, product.title)

    return response


def Order(request):
    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        counter = product_title.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    products=None
    total=0
    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        if product_title != "":
            product_id_in_cart = product_title.split('|')
            products = models.Product.objects.all().filter(id__in = product_id_in_cart)

            for p in products:
                total = total+ p.selling_price
    return render(request,'order.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})


def remove_from_cart_view(request,pk):
    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        counter=product_title.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    total=0
    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        product_id_in_cart=product_title.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.Product.objects.all().filter(id__in = product_id_in_cart)
        for p in products:

            total = total+ p.selling_price

        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request, 'cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart,'redirect_to' : request.GET['next_page']})
        if value=="":
            response.delete_cookie('product_title')
        response.set_cookie('product_title',value)
        return response


def address(request):
    product_in_cart=False
    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        if product_title != "":
            product_in_cart=True
    if 'product_title' in request.COOKIES:
        product_title = request.COOKIES['product_title']
        counter=product_title.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    addressForm = forms.AddressForm()
    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            name = addressForm.cleaned_data['Name']
            email = addressForm.cleaned_data['Email']
            mobile=addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']

            total=0

            if 'product_title' in request.COOKIES:
                product_title = request.COOKIES['product_title']
                if product_title != "":
                    product_id_in_cart=product_title.split('|')
                    products=models.Product.objects.all().filter(id__in = product_id_in_cart)
                    for p in products:
                        total = total + p.selling_price
                    context={
                        "mobile":"0929635322", #seller's mobile
                        "amount": total,
                        'total': total
                    }
            response = render(request, 'payment.html', context)
            response.set_cookie('name',name)
            response.set_cookie('email',email)
            response.set_cookie('mobile',mobile)
            response.set_cookie('address',address.encode('utf-8'))
            return response

    return render(request,'address.html',{'addressForm':addressForm,'product_in_cart':product_in_cart})










