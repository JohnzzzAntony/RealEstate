from django import forms
from .models import Property, PropertyUnit

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class PropertyUnitForm(forms.ModelForm):
    class Meta:
        model = PropertyUnit
        fields = '__all__'
