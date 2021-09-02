from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, ProfileSerializer
from .models import Product, Category, Profile
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q
# Create your views here.


# Default authentication is isAuthenticated
def index(request):
    return render(request, 'home.html')


class ProductList(ListCreateAPIView):
    """
    List all of the products in our database
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class CategoryList(APIView):
    """
    List all of the categories in our database
    """

    def get(self, request):
        categories = Category.objects.all() # Note that these categories are already ordered by name
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileList(ListAPIView):
    """
    List all the profile of our users in the database
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)


# class ProductDetail(APIView):     ## id format
#     """
#     List details about ONE specific product given the product id
#     """
#
#     def get(self, request, product_id):
#         product = Product.objects.get(id=product_id)
#         serializer = ProductSerializer(product, many=False)
#         return Response(serializer.data)

# Slug
class ProductDetail(APIView):
    """
    Provides details about a single product given the category_slug and product_slug
    """

    def get_object(self, category_slug, product_slug):
        # lets check if the obj exist
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    # time to override the get function: make sure to pass in the slugs
    def get(self, request, category_slug, product_slug, format=None):
        # we need to get the product so
        product = self.get_object(category_slug, product_slug)  # so we are using that get_obj function passing in args
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


class CategoryDetail(APIView):
    """
    Provides details about a single category given the category_slug
        1) We need to retrieve the category
        2) Use that category to access all the products that are under those categories
        3) Return them as an array of items
    """

    def get_object(self, category_slug):
        try:
            # return Category.objects.filter(slug=category_slug) <-- using filter gives queryset <- queryset no attr
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        product_category = Product.objects.filter(category=category.id).all()
        serializer = ProductSerializer(product_category, many=True)
        return Response(serializer.data)


class LatestProducts(APIView):
    """
    List the first 5 items that are in our Products model
    """
    def get(self, request):
        latest_products = Product.objects.all()[:5]     # 5 items [start:stop] stop excludes similar to range
        serializer = ProductSerializer(latest_products, many=True)
        return Response(serializer.data)


@api_view(['POST']) # when making an api view you have to specify which methods you want so
def search(request):
    query = request.data.get('query', '')

    if query:
        # We could make some big queries like containing certain words from our query
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'products': []})