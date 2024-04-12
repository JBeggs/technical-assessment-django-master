from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import (
    Camera, 
    CameraGroup, 
    CameraStatusLog,
)
from .serializers import (
    CameraSerializer,
    CameraGroupSerializer,
    CameraStatusLogSerializer,
    CameraMatrixSerializer,
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


class CameraStatusUpdateViewSet(UpdateAPIView):
    """Camera status log update viewset"""
    queryset = CameraStatusLog.objects.all()
    serializer_class = CameraStatusLogSerializer
    permission_classes = [IsAuthenticated]


class CameraMatrixViewSet(viewsets.ModelViewSet):
    """Camera matrix viewset"""
    queryset = Camera.objects.all()
    serializer_class = CameraMatrixSerializer
    
    def list(self, request, *args, **kwargs):
        print(request.data['result'])
