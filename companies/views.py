from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import InternalTenantCompany
from .forms import InternalTenantCompanyForm

class CompanyListView(LoginRequiredMixin, ListView):
    model = InternalTenantCompany
    template_name = 'companies/company_list.html'
    context_object_name = 'companies'

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = InternalTenantCompany
    template_name = 'companies/company_detail.html'

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = InternalTenantCompany
    form_class = InternalTenantCompanyForm
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('company_list')

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = InternalTenantCompany
    form_class = InternalTenantCompanyForm
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('company_list')
