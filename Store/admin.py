from import_export import resources
from django.contrib import admin
from .models import *

# Register your models here.

# class
class BookResource(resources.ModelResource):

    class Meta:
        model = Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
  pass