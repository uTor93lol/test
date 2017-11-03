from django.contrib import admin
from .models import *
# Register your models here.
class ProjectImgInline(admin.TabularInline):
    model = ProjectImg
    extra = 0

class ProjectAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Projects._meta.fields]
    inlines = [ProjectImgInline]
    class Meta:
        model = Projects

admin.site.register(Projects, ProjectAdmin)
