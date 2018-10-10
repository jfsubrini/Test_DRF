"""
API serializers
"""


from rest_framework import serializers

from food.models import Food, Category



class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'brand', 'category', 'nutrition_grade', \
        'nutrition_score', 'url', 'image_food', 'image_nutrition')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
