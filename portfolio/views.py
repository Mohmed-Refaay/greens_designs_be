from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.


class all_sections(APIView):
    def get(self, request):
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data, status=202)


class projects_of_section(APIView):
    def get(self, request, id):
        try:
            section = Section.objects.get(id=id)
            projects = section.projects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=202)
        except:
            return Response({"messge": "This Section is not Found!"}, status=404)


class project_details(APIView):
    def get(self, request, id):
        try:
            project = Project.objects.get(pk=id)
            serializer = ProjectSerializer(project, many=False)
            return Response(serializer.data, status=202)
        except:
            return Response({"messge": "This Section is not Found!"}, status=404)
