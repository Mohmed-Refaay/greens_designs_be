from django.urls import path
from .views import *

urlpatterns = [
    path("sections", AllSections.as_view()),
    path("sections/<id>", ProjectsOfSection.as_view()),
    path("projects/<id>", ProjectDetails.as_view())
]
