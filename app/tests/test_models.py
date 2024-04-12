from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from django_dynamic_fixture import G
from ..models import Camera, CameraStatusLog


class CameraModelTest(TestCase):
    """Test Camera Model"""
    def test_initial_status_log_creation(self):
        """Test intitial status log creation"""
        camera = G(Camera)

        status_logs = CameraStatusLog.objects.filter(camera=camera)

        self.assertEqual(status_logs.count(), 1)
        self.assertEqual(status_logs.first().status, CameraStatusLog.WORKING)


class CameraStatusLogModelTest(TestCase):
    """Test Camera Status Model"""
    
    def test_duration_with_end_date(self):
        """Test Duration with End Date"""
        start_date = timezone.now() - timedelta(days=2)
        end_date = timezone.now() - timedelta(days=1)
        
        camera_log = G(CameraStatusLog, start_date=start_date, end_date=end_date)

        expected_duration = end_date - start_date

        self.assertEqual(camera_log.duration(), str(expected_duration))
