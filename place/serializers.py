from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import Place, Review


class PlaceSerializer(serializers.ModelSerializer):
    lat = serializers.FloatField(write_only=True)
    lon = serializers.FloatField(write_only=True)

    class Meta:
        model = Place
        fields = ["id", "lat", "lon", "location"]

    def create(self, validated_data):
        lat = validated_data.pop("lat")
        lon = validated_data.pop("lon")
        validated_data["location"] = Point(lat, lon)
        return super().create(validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
