"""
API views
"""


from rest_framework import generics

from food.models import Food, Category
from .serializers import FoodSerializer, CategorySerializer



class FoodIdViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows individual product to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows food products to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CategoryViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
