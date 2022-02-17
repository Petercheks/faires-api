from turtle import title
from django.db import models

# Create your models here.


class Task(models.Model):
    # Task Model
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=[
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH')], default='LOW')
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'PENDING'),
        ('IN_PROCESS', 'IN_PROCESS'),
        ('READY', 'READY'),
        ('CANCEL', 'CANCEL'),
        ('ON_HOLD', 'ON_HOLD')], default='PENDING')
    start_date = models.DateTimeField(default=None)
    due_date = models.DateTimeField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class SubTask(models.Model):
    # Sub Task Model
    task = models.ForeignKey(Task, related_name='sub_tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()   
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
