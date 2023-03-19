from django.shortcuts import render
from django.views import View
from home.models.allproducts import AllProducts
from home.models.category import Category
from home.models.cart import Cart


class AllProductView(View):
      def get(self,request):
            allproducts=None
            total_item=0
            category=Category.objects.all()
            categoryID=request.GET.get('category')
            user=request.session.get('customer')
            if user:
                total_item=len(Cart.objects.filter(user=user))

            if categoryID:
                  allproducts=AllProducts.objects.filter(category=categoryID)
            else:
                  allproducts=AllProducts.objects.all()
            data={
                  'allproducts':allproducts,
                  'categories':category,
                  'totalitem':total_item  
            }
            return render(request,'allproduct_view.html',data)

          
     
     




