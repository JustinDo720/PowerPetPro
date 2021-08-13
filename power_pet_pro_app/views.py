from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
# Create your views here.


def index(request):
    return render(request, 'home.html')


class ProductList(APIView):

    def get(self, request, format=None, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer)


class CategoryList(APIView):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer)

