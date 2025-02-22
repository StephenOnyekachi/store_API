
from django.urls import path
from .import views
# from .views import *

urlpatterns = [
    path('users/', views.UsersList.as_view(), name='users'),
    path('userInfo/<int:pk>', views.UserInfo.as_view(), name='userInfo'),

    path('carts/', views.CartList.as_view(), name='carts'),
    path('cartInfo/<int:pk>', views.CartInfo.as_view(), name='cartInfo'),

    path('signUp/', views.SignUp.as_view(), name='signUp'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]