from rest_framework import serializers
from .models import Camera, CameraGroup, CameraStatusLog
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class CameraGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraGroup
        fields = ["id", "name", "description"]


class CameraSerializer(serializers.ModelSerializer):
    group = CameraGroupSerializer(read_only=True)

    class Meta:
        model = Camera
        fields = ["id", "name", "group"]


class CameraStatusLogSerializer(serializers.ModelSerializer):
    camera = CameraSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = CameraStatusLog
        fields = ["id", "camera", "status", "start_date", "end_date", "user"]
