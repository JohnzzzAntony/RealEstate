from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Billing
from .forms import BillingForm

class BillingListView(ListView):
    model = Billing
    template_name = 'billing/billing_list.html'
    context_object_name = 'bills'

class BillingCreateView(CreateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billing/billing_form.html'
    success_url = reverse_lazy('billing_list')
