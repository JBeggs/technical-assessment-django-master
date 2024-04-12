from django.contrib.auth.models import User
from django.urls import reverse
from django_dynamic_fixture import G
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from app.models import CameraGroup, Camera, CameraStatusLog


class ViewsetAuthenticationTest(APITestCase):
    """Authentication tests for endpoints"""
    def setUp(self):
        self.client = APIClient()
        self.authorize()

    def tearDown(self):
        self.client.logout()

    def authorize(self, user=None):
        """Authorize client credentials"""
        user = user or G(User)
        token, _ = Token.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        return user

    def deauthorize(self):
        """Remove client credentials"""
        self.client.credentials()

    def test_camera_viewset_authentication_required(self):
        """Test camera list authentication required"""
        unauthorized_clinet = APIClient()
        url = reverse("camera-list")

        response = unauthorized_clinet.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_camera_group_viewset_authentication_required(self):
        """Test camera group authentication required"""
        unauthorized_clinet = APIClient()
        url = reverse("cameragroup-list")

        response = unauthorized_clinet.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_camera_status_log_viewset_authentication_required(self):
        """Test camera status log authentication required"""
        unauthorized_clinet = APIClient()
        url = reverse("camerastatuslog-list")

        response = unauthorized_clinet.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_camera_viewset_authentication(self):
        """Test camera list"""
        url = reverse("camera-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_camera_list(self):
        """Test camera list response"""
        G(Camera, name="Test")
        url = reverse("camera-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test")

    def test_camera_status_log_update_viewset_authentication_required(self):
        """Test camera status log update authentication required"""
        unauthorized_clinet = APIClient()
        url = reverse("camerastatuslog-update")

        response = unauthorized_clinet.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_camera_status_log_update_viewset(self):
        """Test camera status log update"""
        group = G(CameraGroup, name="Test Group")
        camera = G(Camera, name="Test", group=group)
        G(CameraStatusLog, camera=camera)
        url = reverse("camera-update")

        response = self.client.post(url, data={})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_camera_log_matrix_viewset_authentication_required(self):
        """Test camera log matrix authentication required"""
        unauthorized_clinet = APIClient()
        url = reverse("camera-log-matrix")

        response = unauthorized_clinet.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_camera_log_matrix_viewset(self):
        """Test camera log matrix"""
        group = G(CameraGroup, name="Test Group")
        camera = G(Camera, name="Test", group=group)
        G(CameraStatusLog, camera=camera)
        url = reverse("camera-log-update")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
