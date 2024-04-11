from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CameraViewSet, CameraGroupViewSet, CameraStatusLogViewSet

router = SimpleRouter()
router.register(r"cameras", CameraViewSet)
router.register(r"camera-groups", CameraGroupViewSet)
router.register(r"camera-status-logs", CameraStatusLogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
