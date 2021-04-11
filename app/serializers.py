#Para visualizar nuestras API creamos serializer.py
from rest_framework import serializers
from .models import Product , Promotion

#Creamos la clase de Serializer 
class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields=['id', 'name', 'image', 'description','price']

class ListPromocionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Promotion
        fields=['id','name','cell','email','product','promotion']


