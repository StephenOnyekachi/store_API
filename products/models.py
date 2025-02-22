
from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    is_discount = models.BooleanField(default=False)
    is_avaliable = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

    