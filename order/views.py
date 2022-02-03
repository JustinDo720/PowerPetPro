import stripe
from django.shortcuts import render
from django.conf import settings

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer
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
                currency= 'USD',
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