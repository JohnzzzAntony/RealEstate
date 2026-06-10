from rest_framework import viewsets
from .models import Property, PropertyUnit
from .serializers import PropertySerializer, PropertyUnitSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyUnitViewSet(viewsets.ModelViewSet):
    queryset = PropertyUnit.objects.all()
    serializer_class = PropertyUnitSerializer
