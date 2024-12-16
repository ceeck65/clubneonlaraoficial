from django import forms 
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

# FORMS PROFILES

class ProfileForms(forms.Form):

    GENDER_CHOICES =( 
        ("", "Selecciona Género"),
        ("male", "Masculino"), 
        ("famele", "Femenino"), 
        ("other", "Otro"), 
        ("nothing", "Prefiero no decirlo"), 
    )

    first_name = forms.CharField(label="Nombres", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'}))
    last_name = forms.CharField(label="Apellidos", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido'}))
    birthday = forms.CharField(label="Cumpleaños", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu fecha de cumpleaños'}))
    address = forms.CharField(label="Dirección", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu dirección'}))
    country = CountryField(blank_label="Seleccione País").formfield(widget=CountrySelectWidget(attrs={"class": "form-select form-control"}))
    job = forms.CharField(label="Profesión", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu profesión'}))
    gender = forms.ChoiceField(choices = GENDER_CHOICES, label="Género", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label="Teléfono", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu número de teléfono'}))
    email = forms.EmailField(label="Nombres", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'}))
    social= forms.CharField(label="Redes sociales", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tus redes sociales'}))
    biography = forms.CharField(label="Biografía", required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu biografía', 'rows': 3 }))