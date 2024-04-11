from rest_framework import viewsets
from .models import Camera, CameraGroup, CameraStatusLog
from .serializers import (
    CameraSerializer,
    CameraGroupSerializer,
    CameraStatusLogSerializer,
)


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraGroupViewSet(viewsets.ModelViewSet):
    queryset = CameraGroup.objects.all()
    serializer_class = CameraGroupSerializer


class CameraStatusLogViewSet(viewsets.ModelViewSet):
    queryset = CameraStatusLog.objects.all()
    serializer_class = CameraStatusLogSerializer
