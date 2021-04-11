from django.db import models
from django.contrib.auth.models import User
from authentication.models import User


# Model Producto
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

# Model Promotion
class Promotion(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    cell=models.CharField(max_length=100) #validar que solo sea numeros
    email=models.CharField(max_length=100) #dar formato de correo
    product=models.CharField(max_length=100)
    promotion=models.FloatField() #-10%
    
    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        return self.name

    
# Model Shoping
class ShoppingCart(models.Model):#validar
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ShoppingCart'
        verbose_name_plural = 'ShoppingCarts'

class Order(models.Model):  #validar
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.code

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'OrderDetail'
        verbose_name_plural = 'OrderDetails'
