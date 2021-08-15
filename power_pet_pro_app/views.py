from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.


def index(request):
    return render(request, 'home.html')


class ProductList(ListCreateAPIView):
    """
    List all of the products in our database
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class CategoryList(ListCreateAPIView):
    """
    List all of the categories in our database
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


