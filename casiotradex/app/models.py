from django.db import models
CATAGORY = (('O','Options'),('F','Future'),('E','Equity'));
class Product(models.Model):
    product_image = models.ImageField(upload_to='producting');
    title=models.CharField(max_length=100,default='')
    category = models.CharField(choices=CATAGORY,max_length=2,default='')
class Option(models.Model):
    product_image = models.ImageField(upload_to='producting');
    title=models.CharField(max_length=100,default='')
class SocialMedia(models.Model):
    product_image = models.ImageField(upload_to='producting');
    title=models.CharField(max_length=100,default='')
