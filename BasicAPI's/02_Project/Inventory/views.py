### Application Views.py

from rest_framework .views import APIView
from rest_framework .response import Response
from .models import *
from .serializers import *

class Ourproducts1(APIView):

   def get(self,request):
        full_products = Myproducts.objects.all()
        serialized_products = Products_Serializer1(full_products,many=True).data       ## Many Records
        return Response(serialized_products)


class Ourproducts2(APIView):
    def get(self,request):
        full_products = Myproducts.objects.all()
        serialized_products = Products_Serializer2(full_products,many=True).data       ## Many Records
        return Response(serialized_products)
    

class OurproductsbyID(APIView):
    def get(self,request,id):
        req_product = Myproducts.objects.get(id=id)
        serialized_products = Products_Serializer1(req_product).data     
        return Response(serialized_products)

    def put(self,request,id):
        detail = Myproducts.objects.get(id=id)
        uservalues = request.data

        detail.product_name = uservalues['name']
        detail.code = uservalues['code']
        detail.price = uservalues['price']
        detail.save()
        return Response(f"Updated Product as  {uservalues['name']}")
    
    def delete(self,request,id):
        detail = Myproducts.objects.get(id=id)
        detail.delete()
        return Response(f"Deleted ID {id}")








