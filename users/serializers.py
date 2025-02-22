
from rest_framework import serializers
from .models import Users, Cart

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('__all__')

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('__all__')
