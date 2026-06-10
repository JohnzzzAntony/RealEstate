from rest_framework import serializers
from .models import Subtenant

class SubtenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtenant
        fields = '__all__'
