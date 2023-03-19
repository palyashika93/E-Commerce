from django.db import models
from home.models.allproducts import AllProducts
from home.models.category import Category


class OnSale(models.Model):
    product=models.ForeignKey(AllProducts,on_delete=models.CASCADE)
  
    
