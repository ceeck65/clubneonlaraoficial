from django import forms

from vehicle.models import Vehicle, Brand, TypeVehicle


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ["type_vehicle", "brand", "model", 'year', 'color', 'license_vehicle', 'transmission', 'alias',
                  'number', 'image']

        required = (
            'type_vehicle',
            'brand',
            'model',
            'year',
            'color',
            'license_vehicle',
            'transmission',
        )

        widgets = {
            'type_vehicle': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'license_vehicle': forms.TextInput(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "license_vehicle": "Placa",
        }

        error_messages = {
            'license_vehicle': {
                'unique': ("La placa se encuentra registrada, por favor verifique e intente de nuevo"),
            },
            'number': {
                'unique': ("El número se encuentra asignado a un socio registrado, si crees que se trata de un error comunícate con la directiva del Club Neón Lara Oficial. Puedes dejar el campo vacío para continuar con el registro"),
            },
            'model': {
                'required': ("El módelo de vehiculo es requerido."),
            },
            'color': {
                'required': ("El color de vehiculo es requerido."),
            },
            'year': {
                'required': ("El año de vehiculo es requerido."),
            },
        }



