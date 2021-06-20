from django.contrib import admin
from .models import Event, CollegeName, Comments, SMEProfile


@admin.register(Event)
class EventClass(admin.ModelAdmin):
    pass


@admin.register(CollegeName)
class CollegeNameClass(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsClass(admin.ModelAdmin):
    pass


admin.site.register(SMEProfile)