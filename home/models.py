from django.db import models

# Create your models here.

    


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,default='')
    productname = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.FloatField()
    landmark = models.CharField(max_length=255)

    def __str__(self):
        return f"Order #{self.id}"



class Product(models.Model):
    username = models.CharField(max_length=100,default='')
    product_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')  # Ensure MEDIA_ROOT and MEDIA_URL settings are properly configured

    def __str__(self):
        return self.username
    
class Cart(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.username}"
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name