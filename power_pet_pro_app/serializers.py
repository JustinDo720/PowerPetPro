from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'description',
            'price',
            'date_added',
            # These are for the images
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        )
