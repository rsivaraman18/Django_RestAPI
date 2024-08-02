### Application views.py
from rest_framework .views import APIView
from rest_framework . response import Response
from .models import *
from .serializers import *
 
### Category Foreignkey Connection
class OurCategory(APIView):
    def post(self,request):
        uservalues = request.data
        ProductCategory(category_name=uservalues['category_name']).save()
        return Response ("New Item Saved in Category")
    
    def get(self,request):
        categoryitems =ProductCategory.objects.all()
        serialized_category =  Category_Serializer(categoryitems,many=True).data
        return Response(serialized_category)

    def get(self,request,id):
        categoryitem =ProductCategory.objects.get(id=id)
        serialized_category =  Category_Serializer(categoryitem).data
        return Response(serialized_category)



### Products Serialized Method

class Ourproducts_serial(APIView):
    def post(self,request):
        new_product =  Product_serializer(data=request.data)
        if new_product.is_valid():
            return Response("New Product using Serializer")
        else:
            return Response(new_product.errors)  
         
    def get(self,request):
        viewproducts = Myproducts.objects.all()
        serialized_products =  Product_serializer(viewproducts,many=True).data
        return Response(serialized_products)
    

class Ourproducts_serialBYID(APIView):
    def get(self,request,id):
        viewproducts = Myproducts.objects.get(id=id)
        serialized_products =  Product_serializer(viewproducts).data
        return Response(serialized_products)
    
    def put(self,request,id):
        viewproducts = Myproducts.objects.get(id=id) 
        serialized_data = Product_serializer(viewproducts, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response('Updated')
        return Response('Error in Updating')
    
    def delete(self,request,id):
        product = Myproducts.objects.get(id=id) 
        product.delete()
        return Response("Deleted")
    

        





### Products Manual Method

class Ourproducts_manual(APIView):
    def post(self,request):
        uservalues = request.data
        new_product = Myproducts(product_name=uservalues['product_name'],code=uservalues['code'],price=uservalues['price'] ,category_refrences_id=uservalues['category'])
        new_product.save()
        return Response("New Product  Created by Manual Method")
    

    def get(self,request):
        products = Myproducts.objects.all()
        fullproducts = []
        for each in products:
            singleproduct = {  'product_name' : each.product_name, 'product_code' : each.code, 'product_price':     each.price,'product_id'   : each.id, 'category_id':each.category_refrences_id }
            fullproducts.append(singleproduct)
        return Response(fullproducts)

class Ourproducts_manualBYID(APIView): 
    ### GETBYID
    def get(self,request,id):
        detail = Myproducts.objects.get(id=id)
        product = {  'product_name':detail.product_name,  'product_code':detail.code, 'product_price':detail.price,
                     'product_id': detail.id , 'category_id':detail.category_refrences_id}
        return Response(product)
    
    def put(self,request,id):
        detail    = Myproducts.objects.get(id=id)
        uservalue = request.data
        detail.product_name = uservalue['product_name']
        detail.code         = uservalue['code']
        detail.price        = uservalue['price']
        detail.category_refrences_id        = uservalue['category']
        detail.save()
        return Response('Data Updated Successfully ')
    



    
    

    
