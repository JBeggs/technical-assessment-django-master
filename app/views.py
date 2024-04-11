from rest_framework import viewsets
from .models import Camera, CameraGroup, CameraStatusLog
from .serializers import (
    CameraSerializer,
    CameraGroupSerializer,
    CameraStatusLogSerializer,
)


class CameraViewSet(viewsets.ModelViewSet):
    """Camera viewset"""
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraGroupViewSet(viewsets.ModelViewSet):
    """Camera group viewset"""
    queryset = CameraGroup.objects.all()
    serializer_class = CameraGroupSerializer


class CameraStatusLogViewSet(viewsets.ModelViewSet):
    """Camera status log viewset"""
    queryset = CameraStatusLog.objects.all()
    serializer_class = CameraStatusLogSerializer
