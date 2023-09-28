from django.urls import path, include
from api import views
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', views.ProductView)
router.register(r'categories', views.CategoryView)
