from django.shortcuts import render
from . import models,serializers
from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

class ProjectCategoryView(viewsets.ModelViewSet):
    queryset=models.ProjectCategory.objects.all()
    serializer_class=serializers.ProjectCategorySerializer

    def retrieve(self, request, pk=None):
        category=models.ProjectCategory.objects.get(id=pk)
        projects=models.Projects.objects.filter(category=category).all()
        projectserializer=serializers.ProjectSerializer(projects,many=True,context={'request':request})
        return Response(projectserializer.data)

@api_view(['GET'])
def AllProjects(request):
        projects=models.Projects.objects.all()
        projectserializer=serializers.ProjectSerializer(projects,many=True,context={'request':request})
        return Response(projectserializer.data)
class ProjectView(generics.ListAPIView):
    queryset=models.Projects.objects.all()
    serializer_class=serializers.ProjectSerializer
    
class ContactView(generics.CreateAPIView):
    queryset=models.Contact.objects.all()
    serializer_class=serializers.ContactSerializer


class NewsLetterView(generics.ListCreateAPIView):
    queryset=models.NewsLetter.objects.all()
    serializer_class=serializers.NewsLetterSerializer

