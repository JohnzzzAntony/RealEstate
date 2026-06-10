from rest_framework import serializers
from .models import EjariRegistration

class EjariRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EjariRegistration
        fields = '__all__'
