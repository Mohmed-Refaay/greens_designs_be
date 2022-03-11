from pyexpat import model
from django.contrib import admin

from .models import *

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image


class ProjectAdmin(admin.ModelAdmin):
    inlines =[ImageInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "company")
    readonly_fields = [field.name for field in Contact._meta.fields]
    exclude = ["id"]

admin.site.register(Section)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)

