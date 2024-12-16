from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from vehicle.models import Vehicle
from .forms import ProfileForms

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    vehicle =  Vehicle.objects.filter(user= request.user.id).order_by('id').first()
    return render(request, "backoffice/dashboard.html", {'vehicle': vehicle})




# PROFILES

@login_required(login_url='login')
def profile(request):
    profiles_forms = ProfileForms
    return render(request, "profile/index.html", {'form': profiles_forms})

