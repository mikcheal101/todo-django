from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from warehouse.views import todo_list_views
from warehouse.views import todo_list_item_views

urlpatterns = [
    path('create-todo-list', todo_list_views.create_todo_list,
         name='create-todo-list'),
    path('update-todo-list/<int:id>',
         todo_list_views.update_todo_list, name='update-todo-list'),
    path('delete-todo-list/<int:id>',
         todo_list_views.delete_todo_list, name='delete-todo-list'),
    path('get-all-todo-list', todo_list_views.get_all_todo_list,
         name='get-all-todo-list'),
    path('get-todo-list/<int:id>',
         todo_list_views.get_todo_list, name='get-todo-list'),
    path('create-todo-list-item', todo_list_item_views.create_todo_list_item,
         name='create-todo-list-item'),
    path('update-todo-list-item/<int:id>',
         todo_list_item_views.update_todo_list_item, name='update-todo-list-item'),
    path('delete-todo-list-item/<int:id>',
         todo_list_item_views.delete_todo_list_item, name='delete-todo-list-item'),
    path('get-todo-list-item/<int:id>',
         todo_list_item_views.get_todo_list_item, name='get-todo-list-item'),
    path('get-all-todo-list-item', todo_list_item_views.get_all_todo_list_items,
         name='get-all-todo-list-item'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
