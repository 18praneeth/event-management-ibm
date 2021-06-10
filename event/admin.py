from django.contrib import admin
from .models import Event, CollegeName,SME, Comments


@admin.register(Event)
class EventClass(admin.ModelAdmin):
    pass


@admin.register(CollegeName)
class CollegeNameClass(admin.ModelAdmin):
    pass

@admin.register(SME)
class SME(admin.ModelAdmin):
    pass

@admin.register(Comments)
class CommentsClass(admin.ModelAdmin):
    pass
