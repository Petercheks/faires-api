from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import SubTask, Task
from tasks.serializers import TaskSerializer, SubTaskSerializer


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



class SubTaskViewSet(viewsets.ViewSet):
    
    queryset = SubTask.objects.all()
    
    def retrieve(self, request, pk):
        sub_task = get_object_or_404(SubTask, pk=pk)
        serializer = SubTaskSerializer(sub_task)

        return Response(serializer.data)
    
    def create(self, request):
        sub_task = SubTaskSerializer(data=request.data)

        if sub_task.is_valid():
            sub_task.save()
        else:
            return Response({'datail': 'Bad request.'}, status.HTTP_400_BAD_REQUEST)

        return Response(sub_task.data)
    
    def update(self, request, pk):
        sub_task = get_object_or_404(SubTask, pk=pk)
        serializer = SubTaskSerializer(instance=sub_task, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'datail': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

    def delete(self, request, pk):
        task = get_object_or_404(SubTask, pk=pk)
        task.delete()

        return Response(SubTaskSerializer(task).data)