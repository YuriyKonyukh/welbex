from rest_framework import serializers
from .models import Welbex


class WelbexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welbex
        fields = ('id', 'date', 'name', 'amount', 'distance')