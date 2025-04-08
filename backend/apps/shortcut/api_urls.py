from rest_framework import routers

from apps.shortcut.api_views import ShortcutViewSet

app_name = "shortcut"
router = routers.DefaultRouter()

router.register("", ShortcutViewSet, basename="shortcut")
urlpatterns = router.urls
