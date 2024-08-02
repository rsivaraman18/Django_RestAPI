### Application Serializer.py
from rest_framework import serializers
from .models import *
 
 
class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'    #For all fields in model


class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Myproducts
        fields = '__all__'



