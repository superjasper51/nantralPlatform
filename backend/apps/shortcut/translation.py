from modeltranslation.translator import TranslationOptions, register

from .models import Shortcut


@register(Shortcut)
class ItemTranslationOptions(TranslationOptions):
    fields = ("title", "description")
