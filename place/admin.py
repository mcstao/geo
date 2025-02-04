from django.contrib import admin
from django.contrib.gis.admin.options import GISModelAdmin
from place.models import Place, Review

@admin.register(Place)
class PlaceAdmin(GISModelAdmin):
    default_zoom = 10

admin.site.register(Review)

