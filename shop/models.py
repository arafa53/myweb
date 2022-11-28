from django.utils import timezone
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Main_Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def cat_product(self):
        return self.product_set.all()
    



class Sub_Category(models.Model):
    main_category=models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
        
class Product(models.Model):
    Status=('publish','publish'),('draft','draft')

    product_id=models.AutoField
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Main_Category,on_delete=models.CASCADE,null=True,default="")
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=True,default="")
    price=models.IntegerField(default=0)
    des=models.CharField(max_length=2000)
    status=models.CharField(choices=Status,max_length=200)
    date=models.DateTimeField()
    image=models.ImageField(upload_to="shop/images",default="Status")
    slug=models.CharField(max_length=150)
    def __str__(self):
        return self.name
  


class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.CharField(max_length=55)
    Order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=55)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=10)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    image=models.ImageField(upload_to="shop/images/cust_image")
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=15)
    total=models.CharField(max_length=1000)
    def __str__(self):
        return self.order.user.username





