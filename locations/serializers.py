
from rest_framework import serializers
from .models import State, LocalGovement, Area

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('__all__')


class LocalGovementSerializers(serializers.ModelSerializer):
    class Meta:
        model = LocalGovement
        fields = ('__all__')

class AreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('__all__')
