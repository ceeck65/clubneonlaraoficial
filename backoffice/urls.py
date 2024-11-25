from django.urls import path, include, re_path
from .views import dashboard


urlpatterns = [
    path('admin/', dashboard, name = 'admin'),
    path('admin/dashboard/', dashboard, name = 'dashboard'),
]
