from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from home.models.allproducts import AllProducts
from django.views import View
from home.models.cart import Cart
from home.models.allproducts import AllProducts

class ItemDetailView(View):
    def get(self,request,slug):
        total_item=0
        user=request.session.get('customer')
        if user:
            total_item=len(Cart.objects.filter(user=user))
        product=AllProducts.objects.get(slug=slug)
        print('single_product_id:',product)
        item_already_in_cart=False
        item_already_in_cart=Cart.objects.filter(product=product,user_id=user).exists()
        return render(request,'product_view.html',{'product':product,'item_already_in_cart':item_already_in_cart,'totalitem':total_item})
    

  
    