from django.contrib import admin
from .models import Order
from .models import Product
from .models import Cart
from .models import Message

admin.site.register(Order)
admin.site.register(Message)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.site_header = "Admin AadityaMohit"
admin.site.site_title = "Mohit Admin Portal"
admin.site.index_title = "Welcome to AadityaMohit Portal"
