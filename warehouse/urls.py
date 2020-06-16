from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from warehouse.views import todo_list_views
from warehouse.views import todo_list_item_views

urlpatterns = [
    path('create-todo-list', todo_list_views.create_todo_list,
         name='create-todo-list'),
    path('update-todo-list/<int:id>',
         todo_list_views.update_todo_list, name='update-todo-list'),
    path('-todo-list', todo_list_views., name='-todo-list'),
    path('-todo-list', todo_list_views., name='-todo-list'),
    path('-todo-list', todo_list_views., name='-todo-list'),
]
