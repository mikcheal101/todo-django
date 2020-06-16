from rest_framework.decorators import api_view


@api_view(['GET'])
def get_todo_list(request):
    pass


@api_view(['POST'])
def update_todo_list(request):
    pass


@api_view(['POST'])
def delete_todo_list(request):
    pass


@api_view(['GET'])
def get_all_todo_list(request):
    pass
