from pyexpat import model
from django.contrib import admin

from .models import *

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image


class ProjectAdmin(admin.ModelAdmin):
    inlines =[ImageInline]


admin.site.register(Section)
admin.site.register(Project, ProjectAdmin)

