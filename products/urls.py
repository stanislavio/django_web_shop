from django.urls import path
from products import views


urlpatterns = [
    path('', views.main),
    path('<int:product_id>/', views.detail, name='product_detail')
]
