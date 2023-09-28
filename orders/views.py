from django.contrib.auth.models import User
from rest_framework import generics, serializers, viewsets

from api.views import ProductSerializer
from orders import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class OrderSerializer(serializers.Serializer):
    user = UserSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        fields = ('user', 'products', 'quantity')


class OrderView(viewsets.ModelViewSet):

    queryset = models.Order.objects.all()
    serializer_class = OrderSerializer
