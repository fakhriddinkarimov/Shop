from django.shortcuts import render
from  rest_framework.decorators import api_view,permission_classes
from  rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from  ..models import Product,Order,OrderItem,ShippingAdress
from ..serializers import ProductSerializer

from rest_framework import status


@api_view('POST')
@permission_classes(['IsAuthenticated'])
def addORderItems(request):

    user = request.user
    data = request.data
    orderItems = data['orderItems']
    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST )
    else:
        order = Order.objects.create(
            user = user,
            payment = data['paymentMethod'],
            taxPrice = data['taxPrice'],
            shippingPrice = data['shippingPrice'],
            totalPrice = data['totalPrice'],
        )
    return Response('order')