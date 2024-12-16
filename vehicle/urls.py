from django.urls import path, include
from django.contrib.auth.decorators import login_required
from  vehicle.views import VehicleList, VehicleCreate, VehicleDetail, VehicleUpdate
from django.conf import settings

urlpatterns = [

    path('', login_required(VehicleList.as_view()), name='vehicles'),

    path('new/', login_required(VehicleCreate.as_view()), name='vehicles_new'),
    path('<int:pk>/', login_required(VehicleDetail.as_view()), name='vehicles_detail'),
    path('update/<int:pk>/', login_required(VehicleUpdate.as_view()), name='vehicles_update'),
]