import datetime
import random
from faker import Faker
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status


from warehouse.models import TodoList
from warehouse.models import TodoListItem


class TestRestApi(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('rest/v1/api/', include('warehouse.urls')),
    ]

    def setUp(self):
        self.faker = Faker()

    def test_can_create_todo_list(self):
        """
        Ensure we can create a TodoList Object
        """
        url = reverse('create-todo-list')
        name = self.faker.file_name()
        location = self.faker.file_path()
        data = dict(name=name, location=location)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), name)
        self.assertEqual(response.data.get('location'), location)

    def test_can_update_todo_list(self):
        """
        Ensure we can update a TodoList Object
        """
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(), location=self.faker.file_path())
        url = reverse('update-todo-list', args=[todo_list.id])

        name = self.faker.file_name()
        location = self.faker.file_path()
        data = dict(name=name, location=location)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), name)
        self.assertEqual(response.data.get('location'), location)

    def test_can_delete_todo_list(self):
        """
        Ensure we can delete a TodoList Object
        """
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(), location=self.faker.file_path())
        url = reverse('delete-todo-list', args=[todo_list.id])

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_view_todo_list(self):
        """
        Ensure we can view a TodoList Object
        """
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(), location=self.faker.file_path())
        url = reverse('get-todo-list', args=[todo_list.id])

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_view_all_todo_list(self):
        """
        Ensure we can view all the TodoList Object
        """
        url = reverse('get-all-todo-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_todo_list_item(self):
        """
        Ensure we can create a TodoListItem Object
        """
        url = reverse('create-todo-list-item')

        # random due dates
        month = random.randint(7, 11)
        day = random.randint(1, 28)

        # set max priority
        priority = TodoListItem.HIGH

        # create a dummy TodoList Object
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(),
            location=self.faker.file_path())

        todo_list_item_name = self.faker.sentence()
        todo_list_item_notes = self.faker.paragraph()
        todo_list_item_due_date = datetime.date(2020, month, day)

        # create a sample todo list item post data
        data = dict(
            todo_list=todo_list.id,
            priority=priority,
            name=todo_list_item_name,
            notes=todo_list_item_notes,
            due_date=todo_list_item_due_date
        )

        try:
            response = self.client.post(url, data, format='json')
        except Exception as e:
            print(e)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('priority'), priority)
        self.assertEqual(response.data.get('name'), todo_list_item_name)
        self.assertEqual(response.data.get('notes'), todo_list_item_notes)
        self.assertEqual(response.data.get('due_date'),
                         todo_list_item_due_date.strftime('%Y-%m-%d'))

    def test_can_update_todo_list_item(self):
        """
        Ensure we can update a TodoListItem Object
        """
        # random due dates
        month = random.randint(7, 11)
        day = random.randint(1, 28)

        # set max priority
        priority = TodoListItem.HIGH

        # create a dummy TodoList Object
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(),
            location=self.faker.file_path())

        todo_list_item_name = self.faker.sentence()
        todo_list_item_notes = self.faker.paragraph()
        todo_list_item_due_date = datetime.date(2020, month, day)

        # create a sample TodoListItem
        todo_list_item = TodoListItem.objects.create(
            todo_list=todo_list,
            priority=TodoListItem.LOW,
            name=self.faker.sentence(),
            notes=self.faker.paragraph(),
            due_date=datetime.date(2020, 1, 12))

        # create a sample todo list item post data
        data = dict(
            todo_list=todo_list.id,
            priority=priority,
            name=todo_list_item_name,
            notes=todo_list_item_notes,
            due_date=todo_list_item_due_date
        )
        url = reverse('update-todo-list-item', args=[todo_list_item.id])
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('priority'), priority)
        self.assertEqual(response.data.get('name'), todo_list_item_name)
        self.assertEqual(response.data.get('notes'), todo_list_item_notes)
        self.assertEqual(response.data.get(
            'due_date'), todo_list_item_due_date.strftime('%Y-%m-%d'))

    def test_can_delete_todo_list_item(self):
        """
        Ensure we can delete a TodoListItem Object
        """
        # random due dates
        month = random.randint(7, 11)
        day = random.randint(1, 28)

        # set max priority
        priority = TodoListItem.HIGH

        # create a dummy TodoList Object
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(),
            location=self.faker.file_path())

        todo_list_item_name = self.faker.sentence(),
        todo_list_item_notes = self.faker.paragraph(),
        todo_list_item_due_date = datetime.date(2020, month, day)

        # create a sample TodoListItem
        todo_list_item = TodoListItem.objects.create(
            todo_list=todo_list,
            priority=TodoListItem.LOW,
            name=self.faker.sentence(),
            notes=self.faker.paragraph(),
            due_date=datetime.date(2020, 1, 12))

        url = reverse('delete-todo-list-item', args=[todo_list_item.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_view_todo_list_item(self):
        """
        Ensure we can view a TodoListItem Object
        """
        # random due dates
        month = random.randint(7, 11)
        day = random.randint(1, 28)

        # set max priority
        priority = TodoListItem.HIGH

        # create a dummy TodoList Object
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(),
            location=self.faker.file_path())

        todo_list_item_name = self.faker.sentence(),
        todo_list_item_notes = self.faker.paragraph(),
        todo_list_item_due_date = datetime.date(2020, month, day)

        # create a sample TodoListItem
        todo_list_item = TodoListItem.objects.create(
            todo_list=todo_list,
            priority=TodoListItem.LOW,
            name=self.faker.sentence(),
            notes=self.faker.paragraph(),
            due_date=datetime.date(2020, 1, 12))

        url = reverse('get-todo-list-item', args=[todo_list_item.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_view_all_todo_list_item(self):
        """
        Ensure we can view all TodoListItem Object
        """
        url = reverse('get-all-todo-list-item')
        # random due dates
        month = random.randint(7, 11)
        day = random.randint(1, 28)

        # set max priority
        priority = TodoListItem.HIGH

        # create a dummy TodoList Object
        todo_list = TodoList.objects.create(
            name=self.faker.file_name(),
            location=self.faker.file_path())

        todo_list_item_name = self.faker.sentence(),
        todo_list_item_notes = self.faker.paragraph(),
        todo_list_item_due_date = datetime.date(2020, month, day)

        # create a sample TodoListItem
        todo_list_items = [TodoListItem.objects.create(
            todo_list=todo_list,
            priority=TodoListItem.LOW,
            name=self.faker.sentence(),
            notes=self.faker.paragraph(),
            due_date=datetime.date(2020, 1, 12)) for i in [1, 2, 3]]

        url = reverse('get-all-todo-list-item')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
