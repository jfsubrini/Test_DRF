"""
Api app URL Configuration.
"""


# Django imports
from django.urls import path

# Import from my app
from . import views



urlpatterns = [
    path('product/<int:pk>', views.FoodIdViewSet.as_view()), # URI: /api/product/666
    path('products/', views.FoodViewSet.as_view()), # URI: /api/products/
    path('category/', views.CategoryViewSet.as_view()), # URI: /api/category/
]
