from django.shortcuts import render
from .models import Shop
from .serializers import ShopSerializer
from rest_framework import generics

# Create your views here.


class ShopAPI(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
