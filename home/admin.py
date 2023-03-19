from django.contrib import admin
from home.models.customer import Customer
from home.models.onsale import OnSale
from home.models.allproducts import AllProducts
from home.models.category import Category
from home.models.contact import Contact
from home.models.cart import Cart
from home.models.checkout import Checkout
from home.models.home import WhyChooseUs
from home.models.home import Slider


class AdminCustomer(admin.ModelAdmin):
    list_display=['id','name','email']

class AdminProduct(admin.ModelAdmin):
    list_display=['product_name','product_price','category']

class AdminCart(admin.ModelAdmin):
    list_display=['id','user','product','quantity']   
    
class AdminCheckout(admin.ModelAdmin):
    list_display=['id','customer','product','quantity','address','phone','date','status'] 

admin.site.register(Customer,AdminCustomer)
admin.site.register(OnSale)
admin.site.register(AllProducts,AdminProduct)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Cart,AdminCart)
admin.site.register(Checkout,AdminCheckout)
admin.site.register(WhyChooseUs)
admin.site.register(Slider)
# Register your models here.
