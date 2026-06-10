from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Subtenant
from .forms import SubtenantForm

class SubtenantListView(ListView):
    model = Subtenant
    template_name = 'subtenants/subtenant_list.html'
    context_object_name = 'subtenants'

class SubtenantCreateView(CreateView):
    model = Subtenant
    form_class = SubtenantForm
    template_name = 'subtenants/subtenant_form.html'
    success_url = reverse_lazy('subtenant_list')
