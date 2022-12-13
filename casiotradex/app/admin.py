from django.contrib import admin
from .models import Product,Option,SocialMedia
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['product_image','title']
@admin.register(Option)
class FieldsModelAdmin(admin.ModelAdmin):
    list_display=['product_image','title']
@admin.register(SocialMedia)
class SocialMediaModelAdmin(admin.ModelAdmin):
    list_display=['product_image','title']
