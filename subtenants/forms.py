from django import forms
from .models import Subtenant

class SubtenantForm(forms.ModelForm):
    class Meta:
        model = Subtenant
        fields = '__all__'
