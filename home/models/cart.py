from django.db import models
from .customer import Customer
from .allproducts import AllProducts
from django.shortcuts import reverse
#from django.http.response import HttpResponseRedirect


class Cart(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(AllProducts,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.product_price
    