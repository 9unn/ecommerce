from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced, new
from django.urls import reverse
from django.contrib.auth.models import Group
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','mobile','zipcode','state']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product', 'quantity']
    # def product(self,obj):
    #     link = reverse("admin:app_product_change", args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount', 'rezorpay_order_id','rezorpay_payment_status','rezorpay_payment_id','paid']

# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','customer', 'products', 'quantity','ordered_date','status']
    # def customers(self,obj):
    #     link = reverse("admin:app_customer_change", args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>', link, obj.product.title)
    
    # def products(self,obj):
    #     link = reverse("admin:app_product_change", args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>', link, obj.product.title)
    
    # def payments(self,obj):
    #     link = reverse("admin:app_payment_change", args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>', link, obj.product.title)


admin.site.unregister(Group)

@admin.register(new)
class newModelAdmin(admin.ModelAdmin):
    list_display = [id, 'title','category', 'product_image']

