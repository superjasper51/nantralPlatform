from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.fields.image_field import CustomImageField


# Create your models here.
class Shortcut(models.Model):
    link = models.URLField(max_length=100, verbose_name=_("Address"))
    title = models.CharField(max_length=50, verbose_name=_("Titre de la page"))
    description = models.CharField(
        max_length=255, verbose_name=_("Description du site")
    )
    icon = CustomImageField(verbose_name=_("Logo"))

    def __str__(self):
        return self.title
