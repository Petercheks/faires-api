from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ViewSet):

    queryset = Task.objects.all()

    def list(self, request):
        query = Task.objects.all()
        serializer = TaskSerializer(query, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    def create(self, request):
        task = TaskSerializer(data=request.data)

        if task.is_valid():
            task.save()
        else:
            return Response({'datail': 'Bad request.'}, status.HTTP_400_BAD_REQUEST)

        return Response(task.data)

    def update(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'datail': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()

        return Response(TaskSerializer(task).data)
