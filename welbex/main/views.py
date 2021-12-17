from django.shortcuts import render
from .models import Welbex
from .serializers import WelbexSerializer
from rest_framework import generics


class WelbexListCreate(generics.ListCreateAPIView):
    queryset = Welbex.objects.all()
    serializer_class = WelbexSerializer
# Create your views here.
