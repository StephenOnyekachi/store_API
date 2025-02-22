
# username = models.CharField(max_length=100, blank=True, null=True, unique=False)

from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

from products.models import Products

# Create your models here.

class Users(AbstractUser):
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    balance = models.FloatField(default=0.00, null=True)
    block = models.BooleanField(default=False)
    gender = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='picture', blank=True, null=True)

    def __str__(self):
        return self.username

class Cart(models.Model):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='cart_user')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.IntegerField()
    price = models.IntegerField()
    added = models.DateTimeField(auto_created=True, auto_now=True)
    paid = models.BooleanField(default=False)
    date_paid = models.DateTimeField()

