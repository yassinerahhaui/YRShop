from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
  user = models.ForeignKey(User,related_name='user_product',on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=300)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  old_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
  description = models.TextField(max_length=3000,null=True,blank=True)
  details = RichTextField(null=True,blank=True,config_name='awesome_ckeditor')
  image = models.ImageField(upload_to='',max_length=200,null=True)
  image1 = models.ImageField(upload_to='',max_length=200,null=True,blank=True)
  image2 = models.ImageField(upload_to='',max_length=200,null=True,blank=True)
  image3 = models.ImageField(upload_to='',max_length=200,null=True,blank=True)
  image4 = models.ImageField(upload_to='',max_length=200,null=True,blank=True)
  image5 = models.ImageField(upload_to='',max_length=200,null=True,blank=True)
  # here add images 
  quantity = models.PositiveIntegerField(default=1)
  stock_out = models.BooleanField(default=False)
  sale = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey('Category',related_name='product_category',on_delete=models.PROTECT,null=True)
  collection = models.ForeignKey('Collection',related_name='product_collection',on_delete=models.DO_NOTHING,null=True,blank=True)
  def __str__(self):
    return self.name


class Category(models.Model):
  name = models.CharField(max_length=60)
  icon = models.ImageField(upload_to='',max_length=200,null=True)
  image_header = models.ImageField(upload_to='',max_length=200,null=True)
  def __str__(self):
    return self.name

class Collection(models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User,related_name='user_collection',on_delete=models.CASCADE,null=True)
  category = models.ForeignKey('Category',related_name='collection_category',on_delete=models.PROTECT,null=True)
  image = models.ImageField(upload_to='',max_length=200,null=True)
  description = models.TextField(max_length=3000,null=True,blank=True)
  def __str__(self):
    return self.name
