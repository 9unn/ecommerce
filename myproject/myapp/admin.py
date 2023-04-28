from django.contrib import admin
from .models import *
from django.urls import reverse
from django.contrib.auth.models import Group



# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','customer_id','address','city','province','zipcode','mobile']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','selling_price','quantity']
    # def product(self,obj):
    #     link = reverse("admin:app_product_change", args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount', 'rezorpay_order_id','rezorpay_payment_status','rezorpay_payment_id','paid']

# class TransactionAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Transaction, TransactionAdmin)

class OrderAdmin(admin.ModelAdmin):
    # pass
    list_display = ['user', 'order_ids', 'product']
admin.site.register(Order, OrderAdmin)
# class TransactionAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Transaction, TransactionAdmin)

# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','customer', 'products', 'quantity','ordered_date','status','name','address','city','province','zipcode']
#     def customers(self,obj):
#         link = reverse("admin:app_customer_change", args=[obj.product.pk])
#         return render('<a href="{}">{}</a>', link, obj.product.title)
    
#     def products(self,obj):
#         link = reverse("admin:app_product_change", args=[obj.product.pk])
#         return render('<a href="{}">{}</a>', link, obj.product.title)
    
#     def payments(self,obj):
#         link = reverse("admin:app_payment_change", args=[obj.product.pk])
#         return render('<a href="{}">{}</a>', link, obj.product.title)


admin.site.unregister(Group)

# @admin.register(new)
# class newModelAdmin(admin.ModelAdmin):
#     list_display = [id, 'title','category', 'product_image']

