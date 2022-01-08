from rest_framework import generics

from .models import Nomenclature
from .serializers import NomenclatureSerializer


class NomenclatureList(generics.ListAPIView):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer


class NomenclatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer
