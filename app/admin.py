from django.contrib import admin
from .models import Camera, CameraGroup, CameraStatusLog


class CameraAdmin(admin.ModelAdmin):
    """Admin for Camera"""


class CameraGroupAdmin(admin.ModelAdmin):
    """Admin for Camera"""


class CameraStatusLogAdmin(admin.ModelAdmin):
    """Admin for Camera"""


admin.site.register(Camera, CameraAdmin)
admin.site.register(CameraGroup, CameraGroupAdmin)
admin.site.register(CameraStatusLog, CameraStatusLogAdmin)
