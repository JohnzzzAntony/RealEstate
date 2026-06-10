from rest_framework import viewsets
from .models import Subtenant
from .serializers import SubtenantSerializer

class SubtenantViewSet(viewsets.ModelViewSet):
    queryset = Subtenant.objects.all()
    serializer_class = SubtenantSerializer
