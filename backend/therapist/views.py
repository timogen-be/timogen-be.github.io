from therapist.models import Therapist
from therapist.serializers import TherapistSerializer
from rest_framework import generics


class TherapistList(generics.ListCreateAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer


class TherapistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer
