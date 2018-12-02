from rest_framework import serializers
from .models import Cargo

class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
