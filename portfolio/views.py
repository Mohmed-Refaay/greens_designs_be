from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.


class AllSections(APIView):
    def get(self, request):
        sections = Section.objects.all()
        sections_json_data = list(sections.values())
        return Response(sections_json_data, status=202)


class ProjectsOfSection(APIView):
    def get(self, request, id):
        try:
            section = Section.objects.get(pk=id)
            projects_data = list(section.projects.all().values())

            data = []
            for project in projects_data:
                data.append({
                    "id": project["id"],
                    "title": project["title"],
                    "cover_image": project["cover_image"]
                })

            return Response(data, status=202)
        except:
            return Response({"messge": "This Section is not Found!"}, status=404)


class ProjectDetails(APIView):
    def get(self, request, id):
        try:
            project = Project.objects.get(id=id)
            serializer = ProjectSerializer(project, many=False)
            return Response(serializer.data, status=202)
        except:
            return Response({"messge": "This project is not Found!"}, status=404)


class AddContact(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=202)
        else:
            return Response({"message": "Please enter valid data!"}, status=400)
