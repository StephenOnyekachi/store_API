
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from .serializers import UsersSerializers, CartSerializers
from .models import Users, Cart

# Create your views here.

class SignUp(APIView):
    def post(self, request):
        serializer = UsersSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message':'user created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message':'login successfully'}, status=status.HTTP_201_CREATED)
        return Response(CartSerializers, status=status.HTTP_400_BAD_REQUEST)
    
class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message':'logged out successfully'}, status=status.HTTP_200_OK)

class UsersList(generics.ListCreateAPIView):
    serializer_class = UsersSerializers

    def get_queryset(self):
        queryset = Users.objects.all()
        users = self.request.query_params.get(queryset)
        if users is not None:
            queryset = queryset.filter(users=users)
        return queryset
    
class UserInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsersSerializers
    queryset = Users.objects.all()


class CartList(generics.ListCreateAPIView):
    serializer_class = CartSerializers

    def get_queryset(self):
        queryset = Cart.objects.all()
        carts = self.request.query_params.get(queryset)
        if carts is not None:
            queryset = queryset.filter(carts=carts)
        return queryset
    
class CartInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializers
    queryset = Cart.objects.all()

