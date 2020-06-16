import datetime
import random

from django.test import TestCase
from faker import Faker

from warehouse.models import TodoList, TodoListItem


class TestModels(TestCase):

    def setUp(self):
        # initialize faker
        self.faker = Faker()

        # random due dates
        month = random.randint(7, 11)
        day = random.randint(1, 28)

        # set max priority
        priority = TodoListItem.HIGH

        # create a sample to do list
        todo_list = TodoList.objects.create(name=self.faker.file_name(),
                                            location=self.faker.file_path())

        # create a sample todo list item
        TodoListItem.objects.create(
            todo_list=todo_list, priority=priority, name=self.faker.sentence(), notes=self.faker.paragraph(), due_date=datetime.date(2020, month, day))

    def test_can_update_todo_list(self):
        name = self.faker.file_name()
        location = self.faker.file_path()

        todo_list = TodoList.objects.all().first()
        todo_list.name = name
        todo_list.location = location
        todo_list.save()

        self.assertEqual(todo_list.name, name)
        self.assertEqual(todo_list.location, location)

    def test_can_update_todo_list_item(self):
        # random due dates
        month = 8
        day = 21

        # set low priority
        priority = TodoListItem.LOW

        due_date = datetime.date(2020, month, day)
        name = self.faker.sentence()
        notes = self.faker.paragraph()

        todo_list_item = TodoListItem.objects.all().first()
        todo_list_item.due_date = due_date
        todo_list_item.priority = priority
        todo_list_item.name = name
        todo_list_item.notes = notes
        todo_list_item.save()

        self.assertEqual(todo_list_item.due_date, due_date)
        self.assertEqual(todo_list_item.priority, priority)
        self.assertEqual(todo_list_item.name, name)
        self.assertEqual(todo_list_item.notes, notes)

    def test_can_delete_todo_list(self):
        todo_lists = TodoList.objects.all()
        before_delete_count = todo_lists.count()
        todo_lists.first().delete()
        after_delete_count = todo_lists.count()

        self.assertGreater(before_delete_count, after_delete_count)

    def test_can_delete_todo_list_item(self):
        todo_list_items = TodoListItem.objects.all()
        before_delete_count = todo_list_items.count()
        todo_list_items.first().delete()
        after_delete_count = todo_list_items.count()

        self.assertGreater(before_delete_count, after_delete_count)
