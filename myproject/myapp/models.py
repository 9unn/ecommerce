from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.

CATEGORY_SIZE = (
    ('Xs','Xs'),
    ('S','S'),
    ('M','M'),
    ('L','L'),
)

CATEGORY_CHOICES = (
    ('TO','Top'),
    ('SK','Skirt'),
    ('PA','Pants'),
    ('SH','Shorts'),

)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.PositiveIntegerField()
    discription = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    size = models.CharField(choices=CATEGORY_SIZE ,max_length=2)
    product_image = models.ImageField(upload_to='images')
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ("myapp:products", kwargs={'slug':self.slug})
    

class Customer(models.Model):
    customer_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    rezorpay_order_id = models.CharField(max_length=100, blank=True,null=True)
    rezorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    rezorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')


class Top(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.PositiveBigIntegerField()
    discription = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    size = models.CharField(choices=CATEGORY_SIZE ,max_length=2)
    product_image = models.ImageField(upload_to='images')
   
    def __str__(self):
        return self.title
    
class bestseller(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.PositiveBigIntegerField()
    discription = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    size = models.CharField(choices=CATEGORY_SIZE ,max_length=2)
    product_image = models.ImageField(upload_to='images')
   
    def __str__(self):
        return self.title
    
class new(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.PositiveBigIntegerField()
    discription = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    size = models.CharField(choices=CATEGORY_SIZE ,max_length=2)
    product_image = models.ImageField(upload_to='images')
   
    def __str__(self):
        return self.title
    
class Order(models.Model):
    order_ids = models.PositiveBigIntegerField()
    selling_price = models.PositiveBigIntegerField()
    