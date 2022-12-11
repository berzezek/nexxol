from rest_framework import serializers

from catalog.models import Category, ProductLubricant as Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}}

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'brand',
            'description',
            'price',
            'discount',
            'isActive',
            'image',
            'category',
            'volume',
            'get_unit',
            'get_thumbnail',
            'thumbnail',
            'created_at',
        )


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'brand',
            'description',
            'price',
            'discount',
            'isActive',
            'category',

        )
        extra_kwargs = {'category': {'required': False}, 'name': {'required': False}}
