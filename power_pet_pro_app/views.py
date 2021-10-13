from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, ProfileSerializer, CustomUserSerializer, \
    CartItemSerializer
from .models import Product, Category, CartItem
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework_simplejwt.views import TokenObtainPairView
from power_pet_pro_app.serializers import MyTokenObtainPairSerializer
from django.conf import settings
from users.models import Profile

# Error Handling
from django.http import Http404, HttpResponse
from django.db import IntegrityError
from rest_framework import status


# Create your views here.


# Default authentication is isAuthenticated
def index(request):
    return render(request, 'home.html')


def activate_acc(request, uid, token):
    if uid and token:
        frontend_url = f'{settings.FRONTEND_BASE_URL}activate/{uid}/{token}'
        return redirect(frontend_url)


def reset_password(request, uid, token):
    if uid and token:
        frontend_url = f'{settings.FRONTEND_BASE_URL}password/reset/confirm/{uid}/{token}'
        return redirect(frontend_url)


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
        categories = Category.objects.all()  # Note that these categories are already ordered by name
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
        latest_products = Product.objects.all()[:5]  # 5 items [start:stop] stop excludes similar to range
        serializer = ProductSerializer(latest_products, many=True)
        return Response(serializer.data)


@api_view(['POST'])  # when making an api view you have to specify which methods you want so
def search(request):
    query = request.data.get('query', '')

    if query:
        # We could make some big queries like containing certain words from our query
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'products': []})


# Admin use only
class PostProduct(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserProfile(APIView):
    """
        Returns details about the user's profile page
            - Lets user modify things like address city and stuff
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, user_id):
        return Profile.objects.get(id=user_id)

    def get(self, request, user_id):
        user_profile = self.get_object(user_id)
        serializer = ProfileSerializer(user_profile, many=False)
        return Response(serializer.data)

    def put(self, request, user_id, *args, **kwargs):
        user_profile = self.get_object(user_id)
        profile_serializer = ProfileSerializer(user_profile, data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCart(APIView):
    """
    Provides details about the users cart.
        - List all the items
        - Returns a total amount for usage
        - Allows posting cart items to the correct user
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, user_id):
        # lets check if the obj exist
        try:
            return CartItem.objects.filter(profile=user_id)
        except CartItem.DoesNotExist:
            raise Http404

    # time to override the get function: make sure to pass in the user_id
    def get(self, request, user_id, format=None):
        # we need to get the profile so we will be using user_id for filtering
        cart = self.get_object(user_id)  # so we are using that get_obj function passing in args
        serializer = CartItemSerializer(cart, many=True)
        return Response(serializer.data)

    # # lets handle posting cart items to user cart
    # def post(self, request, user_id, format=None):
    #     # since we are just posting a cart object we wont need the user_id here
    #     serializer = CartItemSerializer(data=request.data)
    #     # heres where we actually handle the post request
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # # lets handle posting cart items to user cart
    # def put(self, request, user_id, format=None):
    #     # since we are just posting a cart object we wont need the user_id here
    #     serializer = CartItemSerializer(data=request.data)
    #     # heres where we actually handle the post request
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT', 'DELETE'])  # when making a function based api view you have to specify which methods you want
def updateUserCart(request, user_id, product_id):
    try:
        product = CartItem.objects.filter(profile=user_id).get(product=product_id)
    except CartItem.DoesNotExist:
        # if product does not exist but we are posting then we will pass the exception otherwise its a put or delete
        if request.method == 'POST':
            pass
        else:
            # if the method is put or delete then we need a product which means we will raise an Http404
            raise Http404

    if request.method == 'POST':
        # For post we dont need our main serializer because we are not changing a specific product we are just adding
        post_serializer = CartItemSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Resposne(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        main_serializer = CartItemSerializer(prodpostuct, many=False, data=request.data)
        if main_serializer.is_valid():
            main_serializer.save()
            return Response(main_serializer.data)
        return Resposne(main_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response({"Success": "You have deleted an item from your cart."}, status=status.HTTP_400_BAD_REQUEST)
