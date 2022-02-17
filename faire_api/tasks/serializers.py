from rest_framework import serializers

from tasks.models import Task, SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    sub_tasks = SubTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
        