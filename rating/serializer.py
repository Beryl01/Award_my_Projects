from rest_framework import serializers
from .models import Profiles,Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('id','name', 'bio', 'projects', 'dp')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id','project_name', 'description')