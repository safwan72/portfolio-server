from rest_framework import serializers
from . import models


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectCategory
        fields = "__all__"
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = "__all__"
        depth = 1


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"
        depth = 1


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsLetter
        fields = "__all__"
        depth = 1
