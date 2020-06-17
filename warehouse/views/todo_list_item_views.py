from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from warehouse.models import TodoListItem
from warehouse.serializers.todo_list_item_serializer import \
    TodoListItemSerializer


@api_view(['GET'])
def get_todo_list_item(request, id):
    todo_list_item = TodoListItem.objects.get(id=id)
    serializer = TodoListItemSerializer(todo_list_item)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_todo_list_item(request):
    serializer = TodoListItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_todo_list_item(request, id):
    todo_list_item = TodoListItem.objects.get(id=id)
    serializer = TodoListItemSerializer(todo_list_item, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def delete_todo_list_item(request, id):
    todo_list_item = TodoListItem.objects.get(id=id)
    todo_list_item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_todo_list_items(request):
    todo_list_item = TodoListItem.objects.order_by('id')
    serializer = TodoListItemSerializer(todo_list_item, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
