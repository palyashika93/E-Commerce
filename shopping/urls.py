from django.contrib import admin
from django.urls import path
from .import settings
from django.conf.urls.static import static
from home.middlewares.auth import auth_middleware
from shopping.views import login,register,contact

from .views.product_view import ItemDetailView
from .views.allproducts import AllProductView
from .views.addtocart import Add_to_cart
from .views.addtocart import Cart_View
from .views.addtocart import Checkout_Order
from .views.addtocart import Myorders
from .views.home import Home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home.as_view(),name='home'),
  
    path('register/',register.register,name='register'),
    path('login/',login.login,name='login'),
    path('logout/',login.logout,name='logout'),
    path('contact/',contact.contact,name='contact'),

    path('allproducts/',auth_middleware(AllProductView.as_view()),name='allproducts'),
 
    path('productpanel/<slug>/',ItemDetailView.as_view(),name='productpanel'),
    path('addtocart/',Add_to_cart.as_view(),name='addtocart'),
    path('cart/',Cart_View.as_view(),name='cart'),
    path('checkout/',Checkout_Order.as_view(),name='checkout'),
    path('myorders/',auth_middleware(Myorders.as_view()),name='myorders')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
