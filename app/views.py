from django.utils import timezone

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

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
    CameraStatusUpdateSerializer
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


class CameraStatusUpdateViewSet(viewsets.ModelViewSet):
    """Camera status log update viewset"""
    queryset = CameraStatusLog.objects.all()
    serializer_class = CameraStatusUpdateSerializer

    def create(self, request, *args, **kwargs):
        
        camera_id = request.data.get('camera_id')
        _status = request.data.get('status')

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid() and camera_id:
            camera = Camera.objects.get(id=camera_id)
            
            previous_log = CameraStatusLog.objects.filter(camera__id=camera_id).latest("id")

            now = timezone.now()

            if previous_log:
                previous_log.end_date = now
                previous_log.save()

            if previous_log.status == _status:
                return Response(data={"error": "cannot update status, no change"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.is_valid(raise_exception=True)
            serializer.save(camera=camera, user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CameraMatrixViewSet(viewsets.ModelViewSet):
    """Camera matrix viewset"""
    queryset = CameraStatusLog.objects.all()
    serializer_class = CameraMatrixSerializer
