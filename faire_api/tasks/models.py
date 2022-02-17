from turtle import title
from django.db import models

# Create your models here.

class Task(models.Model):
    # Task Model
    title = models.CharField(max_length=100)
    description = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class SubTask(models.Model):
    # Sub Task Model
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()   
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)