"""
Api app URL Configuration.
"""


# Django imports
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Import from my app
from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
# http://localhost:8000/api/product/666
# router.register(r'product/<int:product_id>', views.FoodIdViewSet)
# http://localhost:8000/api/product/
router.register(r'product', views.FoodViewSet)
# http://localhost:8000/api/category/
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
