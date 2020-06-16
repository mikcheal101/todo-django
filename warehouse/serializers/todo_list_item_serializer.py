from rest_framework import serializers

from warehouse.models import TodoListItem


class TodoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListItem
        fields = ['todo_list', 'priority', 'name', 'notes', 'due_date', ]
