from rest_framework import generics

from .models import Nomenclature, Location, Patho
from .serializers import NomenclatureSerializer, LocationSerializer, PathoSerializer


class NomenclatureList(generics.ListAPIView):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer


class NomenclatureDetail(generics.RetrieveAPIView):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PathoList(generics.ListAPIView):
    queryset = Patho.objects.all()
    serializer_class = PathoSerializer


class PathoDetail(generics.RetrieveAPIView):
    queryset = Patho.objects.all()
    serializer_class = PathoSerializer
