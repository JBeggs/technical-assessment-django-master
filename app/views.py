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
    serializer_class = CameraStatusLogSerializer

    def create(self, request, *args, **kwargs):
        
        camera_id = request.data.get('camera_id')
        camera = Camera.objects.get(id=camera_id)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            serializer.save(camera=camera, user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CameraMatrixViewSet(viewsets.ModelViewSet):
    """Camera matrix viewset"""
    queryset = Camera.objects.all()
    serializer_class = CameraMatrixSerializer
    
    def list(self, request, *args, **kwargs):
        print(request.data['result'])
