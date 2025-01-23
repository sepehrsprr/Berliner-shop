from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,default="",blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,default=0,decimal_places=2)

    image = models.ImageField(upload_to="upload/product/")
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10,default=0,decimal_places=2)
    rate = models.IntegerField(default=0,blank=True,null=True,validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200,default="",blank=True,null=True)
    phone = models.CharField(max_length=12,default="",blank=True,null=True)
    date = models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product