from django.db import models

# Create your models here.

class TodoList(models.Model):
    class Meta:
        verbose_name = 'todo list'
        verbose_name_plural = 'todo lists'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, unique=True)
    
