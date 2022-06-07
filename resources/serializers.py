from pyexpat import model
from .models import Shop, CoffeeTypes
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_gis.fields import GeometryField


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeTypes
        fields = ('name',)


class ShopSerializer(GeoFeatureModelSerializer):
    types_of_coffee = TypeSerializer(many=True)

    class Meta:
        model = Shop
        geo_field = "location"
        fields = ('name', 'types_of_coffee', 'street_name')
