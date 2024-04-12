from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Camera, CameraGroup, CameraStatusLog


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    class Meta:
        """User serializer meta data"""
        model = User
        fields = ["id", "username"]


class CameraGroupSerializer(serializers.ModelSerializer):
    """Camera group serializer"""
    class Meta:
        """Camera group meta data"""
        model = CameraGroup
        fields = ["id", "name", "description"]


class CameraSerializer(serializers.ModelSerializer):
    """Camera serializer"""
    group = CameraGroupSerializer(read_only=True)

    class Meta:
        """Camera serializer meta data"""
        model = Camera
        fields = ["id", "name", "group"]


class CameraStatusLogSerializer(serializers.ModelSerializer):
    """Camera status log data"""
    camera = CameraSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        """Camera status log serializer meta data"""
        model = CameraStatusLog
        fields = ["id", "camera", "status", "start_date", "end_date", "user"]


class CameraStatusUpdateSerializer(serializers.ModelSerializer):
    """Camera status log data"""
    camera = CameraSerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        """Camera status log serializer meta data"""
        model = CameraStatusLog
        fields = ["camera", "status", "start_date", "end_date", "user"]


class CameraMatrixSerializer(serializers.ModelSerializer):
    """Camera status log data"""
    camera = CameraSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        """Camera status log serializer meta data"""
        model = CameraStatusLog
        fields = ["id", "camera", "status", "start_date", "end_date", "duration", "__str__", "user"]
