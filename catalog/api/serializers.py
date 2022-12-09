from rest_framework import serializers

from catalog.models import Category, ProductLubricant


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}}


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = ProductLubricant
        fields = (
            'id',
            'name',
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
        )


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLubricant
        fields = (
            'id',
            'name',
            'brand',
            'description',
            'price',
            'discount',
            'isActive',
            'category',

        )
        extra_kwargs = {'category': {'required': False}, 'name': {'required': False}}
