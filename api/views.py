"""
API views
"""


from ..food.models import Food, Category
from rest_framework import viewsets
from .serializers import FoodSerializer, CategorySerializer



class FoodIdViewSet(viewsets.ModelViewSet, product_id):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Food.objects.get(id=product_id)
    serializer_class = FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
