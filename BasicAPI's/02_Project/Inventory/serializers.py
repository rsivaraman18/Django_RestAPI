### APP serializer.py
from rest_framework import serializers
from .models import *

class Products_Serializer1(serializers.ModelSerializer):

    class Meta:
        model = Myproducts
        fields = '__all__'    #For all fields in model



class Products_Serializer2(serializers.ModelSerializer):

    class Meta:
        model = Myproducts
        fields = ['product_name']    #For single Field