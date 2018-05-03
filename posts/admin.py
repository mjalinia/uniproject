from django.contrib import admin

from . import models

from django_summernote.admin import SummernoteModelAdmin


class PostModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'




admin.site.register(models.Post,PostModelAdmin)
admin.site.register(models.Learn, PostModelAdmin)
