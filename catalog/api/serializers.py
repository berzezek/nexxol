from rest_framework import serializers
from catalog.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}}

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
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

class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model: Product
        fields: '__all__'