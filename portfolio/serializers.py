from pyexpat import model
from rest_framework import serializers

from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)

    class Meta:
        model = Project
        fields = "__all__"
