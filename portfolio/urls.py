from django.urls import path
from .views import *

urlpatterns = [
    path("sections", all_sections.as_view()),
    path("sections/<id>", projects_of_section.as_view()),
    path("projects/<id>", project_details.as_view())
]
