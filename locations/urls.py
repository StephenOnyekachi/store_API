

from django.urls import path
from .import views
# from .views import *

urlpatterns = [
    path('state/', views.StateList.as_view(), name='state'),
    path('stateInfo/<int:pk>/', views.StateInfo.as_view(), name='stateInfo'),
    path('localGovernment/', views.LocalGovementList.as_view(), name='localGovernment'),
    path('localGovernmentInfo/<int:pk>/', views.LocalGovernmentInfo.as_view(), name='localGovernmentInfo'),
    path('area/', views.AreaList.as_view(), name='area'),
    path('areaInfo/<int:pk>/', views.AreaInfo.as_view(), name='areaInfo'),
]