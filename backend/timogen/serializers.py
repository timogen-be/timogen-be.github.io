from rest_framework.serializers import ModelSerializer

from .models import Location, Nomenclature, Patho, Line


class LineSerializer(ModelSerializer):

    class Meta:
        model = Line
        fields = [
            'kind',
            'description',
            'priority',
            'duration',
            'code',
            'fees',
            'bfees_c_p',
            'bfees_nc_p',
            'bfees_c_np',
            'bfees_nc_np',
        ]


class PathoSerializer(ModelSerializer):
    lines = LineSerializer(many=True)

    class Meta:
        model = Patho
        fields = [
            'id',
            'raw',
            'name',
            'delimiters',
            'lines',
        ]


class LocationSerializer(ModelSerializer):
    pathos = PathoSerializer(many=True)
    lines = LineSerializer(many=True)

    class Meta:
        model = Location
        fields = [
            'id',
            'nomenclature',
            'raw',
            'name',
            'pathos',
            'lines',
        ]


class NomenclatureSerializer(ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Nomenclature
        fields = [
            'id',
            'activity',
            'locations',
        ]
