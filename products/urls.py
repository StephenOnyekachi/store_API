
from django.urls import path
from . import views
# from .views import ProductsList, ProductInfo

urlpatterns = [
    path('products/', views.ProductsList.as_view(), name='products'),
    path('productInfo/<int:pk>/', views.ProductInfo.as_view(), name='productInfo'),
]