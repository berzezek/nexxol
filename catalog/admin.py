from django.contrib import admin
from .models import Category, ProductLubricant as Product, Brand, Image


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Image)
