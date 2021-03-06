from rest_framework import serializers

from warehouse.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['name', 'location', ]
