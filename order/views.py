import stripe
from django.shortcuts import render
from django.conf import settings

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, CartItem
from .serializers import OrderSerializer
# Create your views here.


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        for item in serializer.validated_data:
            print(item)
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data)

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency= 'USD',
                description='Charge from Pet Power Pro',
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)