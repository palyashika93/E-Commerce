from django.shortcuts import render
from home.models.onsale import OnSale
from home.models.home import WhyChooseUs
from home.models.home import Slider
from home.models.onsale import AllProducts
from home.models.category import Category
from home.models.cart import Cart
from django.views import View


class Home(View):
    def get(self,request):
        slider=Slider.objects.all()
        whychooseus=WhyChooseUs.objects.all()
        onsale=OnSale.objects.all()
        allproducts=None
        total_item=0

        user=request.session.get('customer')
        if user:
                total_item=len(Cart.objects.filter(user=user))

        category=Category.objects.all()
        categoryID=request.GET.get('category')
        if categoryID:
                allproducts=AllProducts.objects.filter(category=categoryID)
        else:
                allproducts=AllProducts.objects.all()

        data={
            'onsales':onsale,
            'allproducts':allproducts,
            'sliders':slider,
            'whychooseus':whychooseus,
            'totalitem':total_item
            
        }
        return render(request,'index.html',data)
      


