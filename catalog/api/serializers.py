from rest_framework import serializers
from catalog.models import Category, Product


class CategorySerialier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      model = Product
      fields = (
        'id',
        'category',
        'name',
        'description',
        'image_1',
        'image_2',
        'image_3',
        'discount',
        'unit',
        'price',
        'product_mark',
        'isActive',
        'created_at',
        'discount_price',
        'get_thumbnail'
      )

