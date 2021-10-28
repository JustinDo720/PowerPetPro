from rest_framework import serializers
from .models import Category, Product, CartItem, MessageBox
from users.models import CustomUser, Profile
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
        )


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('get_category_name')
    limited_description = serializers.SerializerMethodField('get_limited_description')

    def get_category_name(self, product):
        category = Category.objects.get(id=product.category.id)
        return category.name

    def get_limited_description(self, product):
        if product.description:
            limited_description = product.description[:125]  # 50 characters
            return limited_description
        else:
            return ''

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'category_name',
            'image',
            'name',
            'description',
            'limited_description',
            'price',
            'date_added',
            # These are for the images
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        )


# for ProfileSerializer we need their username so lets create custom field using SerializerMethodField
class ProfileSerializer(serializers.ModelSerializer):
    # creating the SerializerMethodField and grabbing value from function called get_username
    # REMOVED: trailing fields for easy index display on front end
    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')

    def get_username(self, profile):
        # Profile getting the instance we can use to retrieve the username
        username = profile.user.username
        return username

    def get_email(self, profile):
        # Profile getting the instance we can use to retrieve the email
        email = profile.user.email
        return email


    class Meta:
        # Make sure you dont have , after Profile because ERROR: restframework 'tuple' object has no attribute '_meta'
        model = Profile
        fields = (
            'username',
            'date_joined',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'city',
            'country',
            'state',
            'zip_code',
        )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_product_name')
    price = serializers.SerializerMethodField('get_product_price')
    # Make sure the name of the SerializerMethodField is not the same as the function for it
    get_absolute_url = serializers.SerializerMethodField('get_abs_url')

    def get_product_name(self, cart):
        return cart.product.name

    def get_product_price(self, cart):
        return cart.product.price

    # This cannot be get_absolute_url which brings up a config error
    def get_abs_url(self, cart):
        return cart.product.get_absolute_url()

    class Meta:
        model = CartItem
        fields = (
            'profile',
            'product',
            'quantity',
            'name',
            'price',
            'get_absolute_url'
        )


# Custom Register Serializer
class MyUserCreationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password', 're_password')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['user_id'] = self.user.id  # We are going to use this for uuid
        data['is_staff'] = self.user.is_staff

        return data


class MessageBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBox
        fields = (
            'msg',
        )
