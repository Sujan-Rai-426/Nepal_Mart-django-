from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.type
    class Meta:
        verbose_name_plural ='Categories'



class Product(models.Model):
    name =models.CharField(max_length=50,)
    price =models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    image =CloudinaryField(upload_to='Nepal_Mart/uploads/product/')
    description =models.TextField(max_length=150)
    in_sale =models.BooleanField(default=False)
    in_sale_price =models.DecimalField(default=0, decimal_places=2, max_digits=10)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} {' '} {self.category}'




class Customer(models.Model):
    pass

class Order(models.Model):
    pass
    