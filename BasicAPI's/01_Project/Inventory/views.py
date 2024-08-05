### Application views.py
 
from rest_framework .views import APIView
from rest_framework .response import Response
from .models import *
   
 
class Ourproducts(APIView):
    def post(self,request):
        uservalues = request.data
        print(uservalues)
        new_product = Myproducts(product_name=uservalues['product_name'],code=uservalues['code'],price=uservalues['price'] )
        new_product.save()
        return Response("New Data Saved")
    
    def get(self,request):
        products = Myproducts.objects.all()
        fullproducts = []
        for each in products:
            singleproduct = {
                'product_name' : each.product_name,
                'product_code' : each.code,
                'product_price': each.price,
                'product_id'   : each.id, 
            }
            fullproducts.append(singleproduct)

        return Response(fullproducts)
    

        
class Ourproductsbyid(APIView):
    def get(self,request,id):
        detail = Myproducts.objects.get(id=id)
        product = {
                    'product_name':detail.product_name,
                    'product_code':detail.code,
                    'product_price':detail.price,
                    'product_id': detail.id
        }
        return Response(product)
    
    def put(self,request,id):
        detail    = Myproducts.objects.get(id=id)
        uservalue = request.data
        detail.product_name = uservalue['name']
        detail.code         = uservalue['code']
        detail.price        = uservalue['price']
        detail.save()
        return Response('Data Updated Successfully ')
    
    def patch(self,request,id):
        detail    = Myproducts.objects.get(id=id)
        uservalue = request.data
        detail.product_name = uservalue['name']
        detail.code         = uservalue['code']
        detail.price        = uservalue['price']
        detail.save()
        return Response('Data Updated Successfully by Patch ')
    
    def delete(self,request,id):
        detail   = Myproducts.objects.get(id=id)
        detail.delete()
        return Response('Deleted Successfully')

    

