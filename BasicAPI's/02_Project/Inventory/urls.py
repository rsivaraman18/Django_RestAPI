### Application urls.py
from django.contrib import admin
from django.urls import path
from .views import *
  
urlpatterns = [
    path('products1s/', Ourproducts1.as_view()),
    path('products2s/', Ourproducts2.as_view()),
    path('products/<int:id>/', OurproductsbyID.as_view()),
]
