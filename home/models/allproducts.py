from django.db import models
from .category import Category
from django.shortcuts import reverse


class AllProducts(models.Model):
    product_name=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE ,default=1)
    product_price=models.IntegerField()
    product_offer=models.IntegerField()
    product_image=models.ImageField(upload_to='uploads/allproducts/')
    product_brand=models.CharField(max_length=500)
    product_description=models.TextField(default='')
    slug=models.SlugField()

    def get_absolute_url(self):
        return reverse("productpanel",kwargs={'slug': self.slug})

        
    
  
  
    
    @staticmethod
    def get_products_by_id(ids):
        return AllProducts.objects.filter(id=ids)

    @staticmethod
    def get_all_products():
        return AllProducts.objects.all()

    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return AllProducts.objects.filter(category=category_id)
        else:
            return AllProducts.get_all_products();
