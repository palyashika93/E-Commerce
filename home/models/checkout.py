from django.db import models
from home.models.allproducts import AllProducts
from home.models.customer import Customer
import datetime

class Checkout(models.Model):
    product=models.ForeignKey(AllProducts,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200,default='',blank=True)
    phone=models.CharField(max_length=50,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Checkout.objects.filter(customer=customer_id).order_by('-date')   

    @property
    def total_cost(self):
        return self.quantity * self.product.product_price    