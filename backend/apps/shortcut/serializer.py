from rest_framework import serializers

from apps.shortcut.models import Shortcut


class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = ("link", "title", "description", "icon")
