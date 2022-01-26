from .models import Order, CartItem
from rest_framework_simplejwt.serializers import serializers


class CartItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_product_name')
    price = serializers.SerializerMethodField('get_product_price')
    # Make sure the name of the SerializerMethodField is not the same as the function for it
    get_absolute_url = serializers.SerializerMethodField('get_abs_url')
    photo = serializers.SerializerMethodField('get_photo')

    def get_product_name(self, cart):
        return cart.product.name

    def get_product_price(self, cart):
        return cart.product.price

    # This cannot be get_absolute_url which brings up a config error
    def get_abs_url(self, cart):
        return cart.product.get_absolute_url()

    def get_photo(self, cart):
        print(cart.product.get_image())
        return cart.product.get_image()

    class Meta:
        model = CartItem
        fields = (
            'profile',
            'product',
            'quantity',
            'name',
            'price',
            'get_absolute_url',
            'photo',
        )


class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    username = serializers.SerializerMethodField('get_username')

    def get_username(self, order):
        return order.user.username

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'address',
            'email',
            'zipcode',
            'city',
            'country',
            'state',
            'stripe_token',
            'created_at',
            'username',
            'items'

        )

    def create(self, validated_data):
        # So when we pop with a key, the key doesn't have to be at the end (it could be anywhere)
        items_data = validaded_data.pop('items')
        order = Order.objects.create(**validated_data)

        # Now once we create our order  we need to make order items aka cart items
        for item_data in items_data:
            CartItem.objects.create(order=order, **item_data)

        return order

