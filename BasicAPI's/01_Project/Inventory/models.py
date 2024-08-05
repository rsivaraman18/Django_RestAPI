### Application models.py
  
from django.db import models

class Myproducts(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    code         = models.CharField(max_length=200,null=True)
    price        = models.FloatField(default=0) 
   
