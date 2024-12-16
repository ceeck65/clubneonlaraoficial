from django.contrib import admin

# Register your models here.

from .models import Vehicle, TypeVehicle, Brand, MaintenanceVehicle

admin.site.register(Vehicle)
admin.site.register(TypeVehicle)
admin.site.register(Brand)
admin.site.register(MaintenanceVehicle)