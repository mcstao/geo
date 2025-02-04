from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r"places", PlaceViewSet)
router.register(r"reviews", ReviewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
