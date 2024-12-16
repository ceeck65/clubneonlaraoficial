from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView

from .forms import VehicleForm
from vehicle.models import Vehicle, MaintenanceVehicle
from django.shortcuts import get_object_or_404


# Create your views here.

class VehicleList(ListView):

    model = Vehicle
    template_name = "vehicles/index.html"
    context_object_name = "vehicles"
    success_url = reverse_lazy('/admin/vehicles/')

    def get_queryset(self):
        return Vehicle.objects.filter(user= self.request.user.id)


class VehicleDetail(DetailView):
    model = Vehicle
    template_name = "vehicles/vehicle_detail.html"
    context_object_name = "vehicle"


    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the template context,
        now you can use {{ car }} within the template
        """
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['maintenance'] = MaintenanceVehicle.objects.filter(vehicle = pk).order_by('date').first()
        return context



class VehicleCreate(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicles/create.html"
    success_url = reverse_lazy('vehicles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        print("The model object=", self.object)
        return super().form_valid(form)



class VehicleUpdate(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicles/update.html"
    success_url = reverse_lazy('vehicles')
