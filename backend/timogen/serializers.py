from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

from .models import Location, Nomenclature, Patho, Line


class LineSerializer(ModelSerializer):
    class Meta:
        model = Line
        fields = [
            "kind",
            "description",
            "priority",
            "duration",
            "code",
            "fees",
            "bfees_c_p",
            "bfees_nc_p",
            "bfees_c_np",
            "bfees_nc_np",
        ]


class PathoSerializer(ModelSerializer):
    lines = LineSerializer(many=True)

    class Meta:
        model = Patho
        fields = [
            "id",
            "raw",
            "name",
            "breakpoints",
        ]


class SimplePathoSerializer(ModelSerializer):
    lines = LineSerializer(many=True)

    class Meta:
        model = Patho
        fields = ["id", "name", "breakpoints", "lines"]


class LocationSerializer(ModelSerializer):
    pathos = SimplePathoSerializer(many=True)
    lines = LineSerializer(many=True)

    class Meta:
        model = Location
        fields = ["id", "nomenclature", "raw", "name", "pathos", "lines"]


class NomenclatureSerializer(ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Nomenclature
        fields = [
            "id",
            "activity",
            "locations",
        ]
