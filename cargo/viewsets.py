from rest_framework import viewsets
from .models import Cargo
from .serializers import CargoSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

