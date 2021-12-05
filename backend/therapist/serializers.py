from rest_framework.serializers import ModelSerializer

from .models import Therapist


class TherapistSerializer(ModelSerializer):
    class Meta:
        model = Therapist
        fields = [
            'id',
            'name',
            'inami_nb',
            'bank_account',
            'bce',
            'adress',
            'contracted',
        ]
