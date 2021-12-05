from django.urls import path

from rest_framework import routers

from .views import TherapistViewSet


router = routers.DefaultRouter()
router.register('', TherapistViewSet)

urlpatterns = router.urls
