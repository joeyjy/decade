from rest_framework import viewsets
from .models import Depot
from .serializers import DepotSerializer

class DepotViewSet(viewsets.ModelViewSet):
    queryset = Depot.objects.all()
    serializer_class = DepotSerializer
