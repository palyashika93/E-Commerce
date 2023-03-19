
from django.shortcuts import render,redirect
from django.views import View
from home.models.allproducts import AllProducts
from home.models.customer import Customer
from home.models.cart import Cart
from home.models.checkout import Checkout

class Add_to_cart(View): 
    def get(self,request):
            user_id=request.session.get('customer')
            user=Customer.objects.get(id=user_id)
            product_id=request.GET.get('product')
            products=AllProducts.objects.get(id=product_id)
            Cart(user=user,product=products).save()  
            return redirect('/cart')
    
class Cart_View(View):
    def post(self,request):
        user=request.session.get('customer')
        product=request.POST.get('product_id')
        minus=request.POST.get('minus')
        remove_from_cart=request.POST.get('remove_from_cart')
        cart=[p for p in Cart.objects.all() if p.user_id==user] 
        if cart:
            if minus:
                q=Cart.objects.get(product=product,user_id=user)
                if q.quantity > 1:
                    q.quantity -= 1
                    q.save()
                else:
                    q.delete()
            elif remove_from_cart:
                q=Cart.objects.get(product=product,user_id=user)
                q.delete()        
            else:
                q=Cart.objects.get(product=product,user_id=user)
                q.quantity +=1
                q.save()
         
        else:
            cart=[]
            Cart().quantity=1   
          
        print('product_id:',product)
      
        return redirect('/cart')
    
    def get(self,request):
        total_item=0
        user=request.session.get('customer')
        if user:
            total_item=len(Cart.objects.filter(user=user))

        cart=Cart.objects.filter(user=user)
        print('user:',user)
        print('cartobjects',cart)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user_id==user] 
        print('cart',cart_product)
       
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.product_price)
                amount += tempamount
                totalamount=amount+shipping_amount    
            return render(request,'add_to_cart.html',{'carts':cart,'amount':amount,'totalamount':totalamount,'totalitem':total_item})
        else:
            return render(request,'emptycart.html')

class Checkout_Order(View): 
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        user=request.session.get('customer')
    
        cart_items=Cart.objects.filter(user=user)
        for p in cart_items:
            Checkout(product=AllProducts(id=p.product_id),
                     customer=Customer(id=p.user_id),
                     quantity=p.quantity,
                     price=p.product.product_price,
                     address=address,
                     phone=phone).save()
            p.delete()        
            
        print('List are:',address,phone,user,cart_items)
        return redirect('/myorders')
    def get(self,request):
        total_item=0
        user=request.session.get('customer')
        if user:
            total_item=len(Cart.objects.filter(user=user))

        cart_items=Cart.objects.filter(user=user)
          
        print('cart_items',cart_items)
        amount=0.0
        shipping_amount=70.0
        totalamount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user_id==user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.product_price)
                amount += tempamount
            totalamount=amount+shipping_amount    

        return render(request,'checkout.html',{'totalamount':totalamount,'cart_items':cart_items,'totalitem':total_item})

class Myorders(View):
     def get(self,request):
        total_item=0
        customer=request.session.get('customer')
        if customer:
            total_item=len(Cart.objects.filter(user=customer))
        orders=Checkout.get_orders_by_customer(customer)
        print(orders)
        return render(request,"myorders.html",{'orders':orders,'totalitem':total_item})        



        



    

    
