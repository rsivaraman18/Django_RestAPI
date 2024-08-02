## Application models.py
from django.db import models
  
### Parent Model so top
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.category_name

 

### It deponds on Category(Child Model)
class Myproducts(models.Model):
    category_refrences = models.ForeignKey(ProductCategory,null=True,on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=200,null=True)
    code         = models.CharField(max_length=200,null=True)
    price        = models.FloatField(default=0)

    def __str__(self):
        return self.product_name
