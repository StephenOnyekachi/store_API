
from django.shortcuts import render
from rest_framework import generics
from .serializers import StateSerializers, LocalGovementSerializers, AreaSerializers
from .models import State, LocalGovement, Area

# Create your views here.

class StateList(generics.ListCreateAPIView):
    serializer_class = StateSerializers
    def get_queryset(self):
        queryset = State.objects.all()
        state = self.request.query_params.get(queryset)
        if state is not None:
            queryset=queryset.filter(state=state)
        return queryset
    
class StateInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StateSerializers
    queryset = State.objects.all()

class LocalGovementList(generics.ListCreateAPIView):
    serializer_class = LocalGovementSerializers
    def get_queryset(self):
        queryset  = LocalGovement.objects.all()
        localGovement = self.request.query_params.get(queryset)
        if localGovement  is not None:
            queryset=queryset.filter(localGovement=localGovement)
        return queryset
    
class LocalGovernmentInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocalGovementSerializers
    queryset = LocalGovement.objects.all()
    
class AreaList(generics.ListCreateAPIView):
    serializer_class = AreaSerializers
    def get_queryset(self):
        queryset  = Area.objects.all()
        area = self.request.query_params.get(queryset)
        if area  is not None:
            queryset=queryset.filter(area=area)
        return queryset
    
class AreaInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AreaSerializers
    queryset = Area.objects.all()
    
