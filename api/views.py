from rest_framework import generics, serializers, viewsets
from products import models


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'category_name', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', 'parent']


class ProductView(viewsets.ModelViewSet):

    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
