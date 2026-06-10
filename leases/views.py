from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import MainLease, Sublease
from .forms import MainLeaseForm, SubleaseForm

class MainLeaseListView(ListView):
    model = MainLease
    template_name = 'leases/main_lease_list.html'
    context_object_name = 'leases'

class MainLeaseDetailView(DetailView):
    model = MainLease
    template_name = 'leases/main_lease_detail.html'

class MainLeaseCreateView(CreateView):
    model = MainLease
    form_class = MainLeaseForm
    template_name = 'leases/main_lease_form.html'
    success_url = reverse_lazy('main_lease_list')

class SubleaseListView(ListView):
    model = Sublease
    template_name = 'leases/sublease_list.html'
    context_object_name = 'subleases'

class SubleaseCreateView(CreateView):
    model = Sublease
    form_class = SubleaseForm
    template_name = 'leases/sublease_form.html'
    success_url = reverse_lazy('sublease_list')
