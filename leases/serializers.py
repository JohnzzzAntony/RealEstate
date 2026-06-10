from rest_framework import serializers
from .models import MainLease, Sublease

class MainLeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainLease
        fields = '__all__'

class SubleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sublease
        fields = '__all__'
