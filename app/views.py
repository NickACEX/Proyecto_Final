from django.shortcuts import render
#Importamos la vista por defecto para nuestra URL de APIREST
from rest_framework import generics
#Importamos serializer de User
from .serializers import ListProductSerializer , ListPromocionSerializer
#Retornar repuesta a Endpoints
from rest_framework.response import Response
#Para el estatus de HTTP
from rest_framework import status
#Importamos modelos
from .models import Product, Promotion

# View List Products
class ListProductView(generics.GenericAPIView):   
    
    serializer_class=ListProductSerializer
    
    def get(self,request):
        queryset=Product.objects.all()
        serializer=ListProductSerializer(queryset,many=True)
        prod_data=serializer.data
        return Response(prod_data)

# View List Promotion Register
class ListPromotionView(generics.GenericAPIView):
    
    serializer_class=ListPromocionSerializer
    
    def get(self, request):
        queryset=Promotion.objects.all()
        serializer=ListPromocionSerializer(queryset,many=True)
        prod_data=serializer.data
        return Response(prod_data)
    

