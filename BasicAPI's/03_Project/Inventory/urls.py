### Application Urls.py
from django.contrib import admin
from django.urls import path
from .views import *
   
urlpatterns = [
    ### Category with Serializer
    path('category/',           OurCategory.as_view()),
    path('category/<int:id>/',  OurCategory.as_view()),

    ## Products with serializer
    path('ser_products/',           Ourproducts_serial.as_view()),
    path('ser_products/<int:id>/',  Ourproducts_serialBYID.as_view()),

     ## Products without serializer
    path('man_product/',            Ourproducts_manual.as_view()),
    path('man_products/<int:id>/',  Ourproducts_manualBYID.as_view()),

]
