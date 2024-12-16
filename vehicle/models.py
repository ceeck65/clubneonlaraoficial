from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class TypeVehicle(models.Model):

    class Meta:
        verbose_name = 'Tipo de vehiculo'
        verbose_name_plural = 'Tipo de vehiculos'
        ordering = ['id']

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Brand(models.Model):

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Vehicle(models.Model):

    TRANSMISSION_CHOICES = (
        ('manual', 'Manual'),
        ('automatic', 'Automático'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    type_vehicle = models.ForeignKey(TypeVehicle, on_delete=models.CASCADE, related_name='type_vehicle')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    model = models.CharField(max_length=80, default='Neon')
    year = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    license_vehicle = models.CharField(max_length=80, unique=True)
    transmission = models.CharField(choices= TRANSMISSION_CHOICES, max_length=80)
    alias = models.CharField(max_length=80, null=True, blank=True)
    number = models.CharField(max_length=80, null=True, blank=True, unique=True)
    image = models.ImageField(default='vehicles/neon.jpg', upload_to='vehicles/', null=True, blank=True)


    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering = ['id']

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}  - {self.model} - Placa: ({self.license_vehicle})'



class MaintenanceVehicle(models.Model):

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos de vehiculos'
        ordering = ['id']

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')
    motor = models.CharField(max_length=120, null=True, blank=True, default='2.0L 16V')
    km_actual = models.CharField(max_length=120, null=True, blank=True, default='0')
    oil = models.CharField(max_length=120, null=True, blank=True, default='0KM')
    fuel = models.CharField(max_length=120, null=True, blank=True, default='0Lt')
    break_automobile = models.CharField(max_length=120, null=True, blank=True, default='0KM')
    timing_belt = models.CharField(max_length=120, null=True, blank=True, default='0KM')
    observations = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'{self.vehicle.model}  - Fecha: ({self.date})'