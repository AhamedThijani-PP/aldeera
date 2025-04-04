from django.db import models
import os

# Create your models here.
class category(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to='',null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    new_arrival=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        # Delete the image file from the file system before deleting the record
        for product in self.category_product_set.all():  # Access related products
            if product.product_image:
                if os.path.isfile(product.product_image.path):
                    os.remove(product.product_image.path)
            product.delete()
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class category_product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False,blank=False)
    product_image=models.ImageField(upload_to='',null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    new_arrival=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        # Delete the product image from the file system before deleting the record
        if self.product_image:
            if os.path.isfile(self.product_image.path):
                os.remove(self.product_image.path)
        super().delete(*args, **kwargs)

class store(models.Model):
    number=models.CharField(max_length=5,null=False,blank=False)
    loc_add=models.CharField(max_length=100,null=False,blank=False)
    loc_link=models.URLField(max_length=150,null=False,blank=False)
    phone=models.CharField(max_length=30,null=True,blank=True)
    insta_name=models.CharField(max_length=30,null=True,blank=True)
    insta_link=models.URLField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.number