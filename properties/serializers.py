from rest_framework import serializers
from .models import Property, PropertyUnit

class PropertyUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyUnit
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    units = PropertyUnitSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = '__all__'
