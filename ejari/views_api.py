from rest_framework import viewsets
from .models import EjariRegistration
from .serializers import EjariRegistrationSerializer

class EjariRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EjariRegistration.objects.all()
    serializer_class = EjariRegistrationSerializer
