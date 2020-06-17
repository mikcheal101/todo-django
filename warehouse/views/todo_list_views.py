from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from warehouse.models import TodoList

from warehouse.serializers.todo_list_serializer import TodoListSerializer


@api_view(['GET'])
def get_todo_list(request, id):
    todo_list = TodoList.objects.get(id=id)
    serializer = TodoListSerializer(todo_list, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_todo_list(request):
    serializer = TodoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_todo_list(request, id):
    todo_list = TodoList.objects.get(id=id)
    serializer = TodoListSerializer(todo_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def delete_todo_list(request, id):
    todo_list = TodoList.objects.get(id=id)
    todo_list.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_todo_list(request):
    todo_list = TodoList.objects.order_by('id')
    serializer = TodoListSerializer(todo_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
