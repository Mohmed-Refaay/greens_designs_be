from pyexpat import model
from rest_framework import serializers

from .models import *


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = "__all__"
