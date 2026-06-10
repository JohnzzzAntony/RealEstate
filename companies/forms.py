from django import forms
from .models import InternalTenantCompany

class InternalTenantCompanyForm(forms.ModelForm):
    class Meta:
        model = InternalTenantCompany
        fields = '__all__'
