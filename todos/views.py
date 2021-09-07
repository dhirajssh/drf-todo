from django.shortcuts import render
from .models import Task, Group
from users.models import NewUser
from .serializers import TaskSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class GroupList(APIView):

  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = request.user
    groups = Group.objects.filter(user=user)
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    user = request.user
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
      group = serializer.save()
      group.user = user
      group.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

class TaskList(APIView):

  permission_classes = [IsAuthenticated]

  def get(self, request, pk):
    group = Group.objects.get(pk=pk)
    tasks = group.task_set.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, pk):
    group = Group.objects.get(pk=pk)
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
      task = serializer.save()
      task.group = group
      task.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

class TaskDetail(APIView):

  permission_classes = [IsAuthenticated]

  def get_object(self, pk):
    try:
      return Task.objects.get(pk=pk)
    except Task.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def put(self, request, pk):
    task = self.get_object(pk)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  
  def delete(self, request, pk):
    task = self.get_object(pk)
    task.delete()
    return Response({
      "data": "deleted",
      "id": pk,
      "status": "204",
    }, status=status.HTTP_204_NO_CONTENT)
