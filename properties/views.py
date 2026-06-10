from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Property, PropertyUnit
from .forms import PropertyForm, PropertyUnitForm

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'

class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('property_list')

class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('property_list')

class PropertyUnitListView(ListView):
    model = PropertyUnit
    template_name = 'properties/unit_list.html'
    context_object_name = 'units'

class PropertyUnitDetailView(DetailView):
    model = PropertyUnit
    template_name = 'properties/unit_detail.html'

class PropertyUnitCreateView(CreateView):
    model = PropertyUnit
    form_class = PropertyUnitForm
    template_name = 'properties/unit_form.html'
    success_url = reverse_lazy('unit_list')
