from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Place, Review


class PlaceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        geo_field = 'location'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
