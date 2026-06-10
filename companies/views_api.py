from rest_framework import viewsets
from .models import InternalTenantCompany
from .serializers import InternalTenantCompanySerializer

class InternalTenantCompanyViewSet(viewsets.ModelViewSet):
    queryset = InternalTenantCompany.objects.all()
    serializer_class = InternalTenantCompanySerializer
