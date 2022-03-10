from pyexpat import model
from django.contrib import admin

from .models import *

# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines =[ImageInline]

admin.site.register(Section, SectionAdmin)
admin.site.register(Project, ProjectAdmin)

