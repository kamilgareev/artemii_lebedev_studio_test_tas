from rest_framework.serializers import ModelSerializer

from .models import SpecialistsRegistry


class SpecialistsRegistryViewSetSerializer(ModelSerializer):
    class Meta:
        model = SpecialistsRegistry
        fields = '__all__'
