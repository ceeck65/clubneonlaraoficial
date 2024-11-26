from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfileForms

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    return render(request, "backoffice/dashboard.html")


# PROFILES

@login_required(login_url='login')
def profile(request):
    profiles_forms = ProfileForms
    return render(request, "profile/index.html", {'form': profiles_forms})


# PROFILES

@login_required(login_url='login')
def vehicles(request):
    return render(request, "vehicles/index.html")