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
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class TodoListItem(models.Model):

    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'
    NONE = 'NONE'
    PRIORITIES = [
        (HIGH, HIGH),
        (MEDIUM, MEDIUM),
        (LOW, LOW),
        (NONE, NONE),
    ]

    class Meta:
        verbose_name = 'todo list item'
        verbose_name_plural = 'todo lists items'

    def __str__(self):
        return self.name

    priority = models.CharField(
        max_length=200, choices=PRIORITIES, default=HIGH)
    name = models.CharField(max_length=200)
    notes = models.TextField()

    due_date = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
