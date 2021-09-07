from rest_framework import serializers
from .models import Task, Group

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['title', 'description', 'completed', 'id']

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['title', 'id']
