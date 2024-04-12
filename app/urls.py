from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    CameraViewSet, 
    CameraGroupViewSet, 
    CameraStatusLogViewSet,
    CameraStatusUpdateViewSet,
    CameraMatrixViewSet,
)

router = SimpleRouter()
router.register(r"cameras", CameraViewSet)
router.register(r"camera-groups", CameraGroupViewSet)
router.register(r"camera-status-logs", CameraStatusLogViewSet)
router.register(r"camera-matrix", CameraMatrixViewSet, basename='camera-matrix')

urlpatterns = [
    path("", include(router.urls)),
    path(r"camera-status-update/",CameraStatusUpdateViewSet.as_view(), name="camera-status-update"),
    path(r"api-token-auth/", obtain_auth_token)
]
