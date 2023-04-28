from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .forms import LoginForm, RegForm, AddressForm
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, FormView, View
from myapp.models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from myapp.models import Product

# def login(request):
#    if request.method == "POST": 
#        Login = Login(request.POST) 
#        Login =forms.LoginForm(request.POST, request.FILES)
#        if Login.is_valid(): 
            
#             print('Username:', Login.cleaned_data['Username'])
#             print('Password:',Login.cleaned_data['Password'])
            
#             return redirect('products')
#    else: 
#        Login = LoginForm() 
       
#    return render(request, "home.html", {'Login':login})

# class LoginView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('home')

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data["password"]
        usr = authenticate(username=username, password=password)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
        
    def login(request):
        if request.method == "POST": 
            Login = Login(request.POST) 
            Login =forms.LoginForm(request.POST, request.FILES)
            if Login.is_valid(): 
                    
                    print('Username:', Login.cleaned_data['Username'])
                    print('Password:',Login.cleaned_data['Password'])
                    
                    return redirect('products')
        else: 
            Login = LoginForm() 
            
        return render(request, "home.html", {'Login':login})


def reg(request):
   if request.method == "POST": 
       Reg = Reg(request.POST) 
       Reg =forms.RegForm(request.POST, request.FILES)
       if Reg.is_valid(): 
            print('Username:', Reg.cleaned_data['Username'])
            print('Email:', Reg.cleaned_data['Email']) 
            print('Password:',Reg.cleaned_data['Password'])
            
            return redirect('products')
   else: 
       Reg = RegForm() 

   return render(request, "products.html", {'RegForm':reg})

class regView(CreateView):
    template_name = 'register.html'
    form_class = RegForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


# class Home(View):
#     template_name = 'home.html'

def Home(request):
    return render(request,'home.html', {'Home':Home})

# class about(View):
#     template_name = 'about.html'

def about(request):
    return render(request, "about.html", {'about':about})

def account(request):
    return render(request, "account.html", {'account':account})


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "productdetail.html"

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'productdetail.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        # # fetch the object based on a different identifier, e.g. the product code
        # product_code = self.kwargs.get('id')
        # obj = get_object_or_404(queryset, id = product_code)
        # return obj

def productdetail(request):
    productdetail = get_object_or_404(Product, id=1)
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


# class Products(ListView):
#     model = Product
#     template = 'products_list.html'

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)

# def products(request):
#     products = models.Product.objects.all()

    # for p in products:
    #     print(p.title)


    # if 'product_title' in request.COOKIES:
    #     product_title = request.COOKIES['product_title']
    #     counter = product_title.split('|')
    #     product_count_in_cart=len(set(counter)) 

    # else:
    #     product_count_in_cart = 0
    #     context = {
    #     'p': products,
    #     'product_count_in_cart': product_count_in_cart,}
    # # if request.user.is_authenticated:
    #     return HttpResponseRedirect('Products')
    # return render(request,'products_list.html', {'products':products,'product_count_in_cart':product_count_in_cart})


# def top(request):
#     top = models.top.objects.all()
#     if 'tops' in request.COOKIES:
#         tops = request.COOKIES['tops']

#     if request.user.is_authenticated:
#         return HttpResponseRedirect('top')
#     return render(request, "top.html", {'top':top})

# def logout(request):
#     return render(request, "logout.html", {'logout':logout})


# def bestseller(request):
#     bestseller = models.bestseller.object.all()
#     if request.user.is_autheticated:
#         return HttpResponseRedirect('bestseller')
#     return render(request, "home.html", {'bestseller':bestseller})


# def new(request):
#     new = models.new.object.all()
#     if 'new' in request.COOKIES:
#         new = request.COOKIES['new']

#     if request.user.is_autheticated:
#         return HttpResponseRedirect('new')
#     return render(request, "home.html", {'new':new})


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










