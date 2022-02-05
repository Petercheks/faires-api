from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Task
from tasks.serializers import TaskSerializer

# Create your views here.

class TaskViewSet(viewsets.ViewSet):
    
    queryset = Task.objects.all()
    
    def list(self, request):
        query = Task.objects.all()
        serializer = TaskSerializer(query, many=True)

        return Response(serializer.data)    

    def retrieve(self, request, pk):
        query = Task.objects.all()
        task = get_object_or_404(query, pk=pk)
        serializer = TaskSerializer(task)
        
        return Response(serializer.data)