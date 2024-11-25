from django.urls import path, include, re_path
from .views import home, about


urlpatterns = [
    path('', home, name = 'home'),
    path('about/', about, name = 'about'),
]
