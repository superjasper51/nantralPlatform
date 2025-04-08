from rest_framework import permissions, viewsets

from apps.shortcut.models import Shortcut
from apps.shortcut.serializer import ShortcutSerializer


class ShortcutPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class ShortcutViewSet(viewsets.ModelViewSet):
    permission_classes = [ShortcutPermission]
    serializer_class = ShortcutSerializer
    queryset = Shortcut.objects.all()
