from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('elctronics', 'Elctronics'),
        ('computers', 'Computers'),
        ('accessories', 'Accessories'),
        ('furniture', 'Furniture'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)