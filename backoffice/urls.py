from django.urls import path, include, re_path
from .views import dashboard, profile
from django.conf import settings

urlpatterns = [
    path('', dashboard, name = 'admin'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('profile/', profile, name = 'profile'),
    path('vehicles/', include('vehicle.urls')),
]


# Media route

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)