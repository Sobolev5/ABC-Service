from django.contrib import admin

from education.models import Topic
from education.models import Snippet


def enable(modeladmin, request, queryset):
    for object in queryset:
        object.active = True
        object.save()
enable.short_description = "Enable"


def disable(modeladmin, request, queryset):
    for object in queryset:
        object.active = False
        object.save()
disable.short_description = "Disable"


class TopicAdmin(admin.ModelAdmin):
    raw_id_fields = [
        "user_profile",
    ]
    list_display = [f.name for f in Topic._meta.fields]
    list_editable = ["name", "text"]
    actions = [enable, disable]
    save_as = True
admin.site.register(Topic, TopicAdmin)


class SnippetAdmin(admin.ModelAdmin):
    raw_id_fields = [
        "user_profile",
    ]
    list_display = [f.name for f in Snippet._meta.fields]
    list_editable = ["name", "text"]
    actions = [enable, disable]
    save_as = True
admin.site.register(Snippet, SnippetAdmin)