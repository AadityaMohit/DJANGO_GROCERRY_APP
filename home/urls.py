"""grocerry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path('', views.home, name='home'),
   path('contact/', views.contact, name='contact'),
   path('about/', views.about, name='about'),
   path('fruit/', views.fruit, name='fruit'),
path('detergent/', views.detergent, name='detergent'),
   path('cashondelivery/', views.cashondelivery, name='cashondelivery'),
    path('addtocart/', views.addtocart, name='addtocart'),
path('cart/', views.addtocart, name='cart'),  # Assuming you have a separate view function for the cart

    path('ordernow/', views.ordernow, name='ordernow'),
#    path('addtocart/', views.addtocart, name='addtocart'),
   path('cashpay/', views.cashpay, name='cashpay'),
   path('thank/', views.thank, name='thank'),
 path('delete/<int:cart_item_id>/', views.delete_cart_item, name='delete_item'),
path('home/', views.home, name='home'),
path('veggie/', views.veggie, name='veggie'),
path('milk/', views.milk, name='milk'),

path('signup/', views.signup, name='signup'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
path('oil/', views.oil, name='oil'),
path('spice/', views.spice, name='spice'),

path('dal/', views.dal, name='dal'),
path('snacks/', views.snacks, name='snacks'),
# path('register/', views.register, name='register'),
# path('sales/', views.sales, name='sales'),
# path('payment/', views.payment, name='payment'),
# path('card/', views.card, name='card'),
# path('upi/', views.upi, name='upi'),
# path('credit/', views.credit, name='credit'),
# path('netb/', views.netb, name='netb'),
# path('wallet/', views.wallet, name='wallet'),
path('seller/', views.seller, name='seller'),
    path('seller/sform/', views.sform, name='sform'),
    # path(r'^seller/sform/(?P<product_name>[\w\s-]+)/(?P<description>[\w\s-]+)/(?P<price>[\d.]+)/$', views.sform, name='sform'),

]
