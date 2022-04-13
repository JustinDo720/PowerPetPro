import stripe
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from order.pagination import OrderPagination

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Order, OrderItem, Profile
from .serializers import OrderItemSerializer, OrderSerializer, UserOrderSerializer


# Create your views here.


@api_view(['POST'])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('price') for item in serializer.validated_data['items'])

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Pet Power Pro',
                source=serializer.validated_data['stripe_token']
            )

            # NOTE: If the accessToken is not provided during POST request then the request.user is actually anonymous
            serializer.save(paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrder(ListAPIView):
    """
        Given the user id we will fetch their order
            - This includes their items, order id and paid amount
    """
    serializer_class = UserOrderSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = OrderPagination

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Order.objects.filter(user=user_id)  # we don't need to order_by because we already ordered in meta
        return queryset


class LatestUserOrder(APIView):
    """
        Given the user id we will fetch their latest orders
            - We will grab the 3 latest/recent orders
    """

    def get(self, request, user_id):
        order = Order.objects.filter(user=user_id)[:3]
        serializer = UserOrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IndividualUserOrder(APIView):
    """
        Given User id and Order number
            - We will fetch details about their orders and display them fully
                - for instance all of their items
                - address being shipped to
                - total cost etc
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id, order_id):
        order = Order.objects.get(id=order_id, user=user_id)
        serializer = UserOrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IndividualUserOrderItems(ListAPIView):
    """
        Given User id and Order number
            - We will fetch details about their orders and display them fully
                - for instance all of their items
                - address being shipped to
                - total cost etc
    """

    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = OrderPagination  # Although this is OrderPagination we will still be using 5 items so let's reuse

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        order_id = self.kwargs['order_id']

        order = Order.objects.get(user=user_id, id=order_id)
        order_items = OrderItem.objects.filter(order=order, profile=user_id)
        return order_items  # this is our queryset


# since we are using vue let's make this an api view for our success page on the front to call in order to send the mail
@api_view(['GET'])
def send_success_email(request, user_id, order_id):
    user_profile = Profile.objects.get(id=user_id)
    order_link = f'{settings.FRONTEND_BASE_URL}profile/{user_id}/order/{order_id}/'
    feedback_link = f'{settings.FRONTEND_BASE_URL}submit_feedback/'
    email_template = render_to_string('order/email.html',
                                      {'user_profile': user_profile,
                                       'order_number': order_id,
                                       'order_link': order_link,
                                       'feedback_link': feedback_link,
                                       })

    email = EmailMessage(
        f'PetPowerPro Order #{order_id} Summary',
        email_template,
        settings.EMAIL_HOST_USER,
        ['yetok51203@sartess.com'],
        #[user_profile.user.email],
    )

    email.fail_silently = False
    email.content_subtype = "html"
    email.send()
    return Response({'message': "Email has been sent"})


@api_view(['POST'])
def check_order_number(request, order_id):
    if request.data['user_id']:
        if Order.objects.filter(id=order_id, user=request.data['user_id']).exists():
            return Response({'order_exists': True}, status.HTTP_200_OK)

    return Response({'order_exists': False}, status.HTTP_200_OK)