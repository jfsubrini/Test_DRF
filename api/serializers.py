"""
API serializers
"""


from ..models import Food, Category
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'brand', 'category', 'nutrition_grade', \
        'nutrition_score', 'url', 'image_food', 'image_nutrition']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
