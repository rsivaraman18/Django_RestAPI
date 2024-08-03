### Application urls.py
   
from django.urls import path
from .views import * 

urlpatterns = [
    path('products/',          Ourproducts.as_view() ),
    path('products/<int:id>/', Ourproductsbyid.as_view() ),

]
