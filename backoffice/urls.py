from django.urls import path, include, re_path
from .views import dashboard, profile, vehicles


urlpatterns = [
    path('admin/', dashboard, name = 'admin'),
    path('admin/dashboard/', dashboard, name = 'dashboard'),
    path('admin/profile/', profile, name = 'profile'),

    path('admin/vehicles/', vehicles, name='vehicles'),
]
