from rest_framework import serializers
from .models import InternalTenantCompany

class InternalTenantCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalTenantCompany
        fields = '__all__'
