from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post


class PostAdmin(TranslationAdmin):
    group_fieldsets = True

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css', ),
        }


admin.site.register(Post, PostAdmin)

# Register your models here.
