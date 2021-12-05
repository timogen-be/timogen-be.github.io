from rest_framework.viewsets import ModelViewSet

from .models import Therapist
from .serializers import TherapistSerializer

class TherapistViewSet(ModelViewSet):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer
