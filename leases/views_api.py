from rest_framework import viewsets
from .models import MainLease, Sublease
from .serializers import MainLeaseSerializer, SubleaseSerializer

class MainLeaseViewSet(viewsets.ModelViewSet):
    queryset = MainLease.objects.all()
    serializer_class = MainLeaseSerializer

class SubleaseViewSet(viewsets.ModelViewSet):
    queryset = Sublease.objects.all()
    serializer_class = SubleaseSerializer
