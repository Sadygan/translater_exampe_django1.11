from modeltranslation.translator import translator, TranslationOptions
from .models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


translator.register(Post, PostTranslationOptions)