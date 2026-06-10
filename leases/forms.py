from django import forms
from .models import MainLease, Sublease

class MainLeaseForm(forms.ModelForm):
    class Meta:
        model = MainLease
        fields = '__all__'

class SubleaseForm(forms.ModelForm):
    class Meta:
        model = Sublease
        fields = '__all__'
