"""
Api app URL Configuration.
"""


# Django imports
from django.urls import path


# Import from my app
from . import views



urlpatterns = [
    path('product/id/<int:product_id>', views.FoodIdViewSet.as_view(), name='product_get'),
    # path('product/create', views.product_create, name='product_create'),
    path('product/search', views.FoodViewSet.as_view(), name='product_search'),
    path('category/search', views.CategoryViewSet.as_view(), name='category_search'),
]
