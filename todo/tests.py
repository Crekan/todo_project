from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskListTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='qweasdqweasd')
        self.task1 = Task.objects.create(title='Test Task 1', description='Test Description 1', user=self.user)
        self.task2 = Task.objects.create(title='Test Task 2', description='Test Description 2', user=self.user)

    def test_tasl_list_view(self):
        self.client.login(username='test', password='qweasdqweasd')
        response = self.client.get(reverse('todo:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)
        self.assertTemplateUsed(response, 'todo/task_list.html')


class TaskCreateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='qweasdqweasd')

    def test_task_create_view(self):
        self.client.login(username='test', password='qweasdqweasd')
        response = self.client.post(reverse('todo:task_create'), {
            'title': 'Test Task',
            'description': 'Test Description',
            'completed': False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('todo:task_list'))
        self.assertTrue(Task.objects.filter(title='Test Task').exists())


class TaskUpdateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='qweasdqweasd')
        self.task = Task.objects.create(title='Test Title', description='Test Description', user=self.user)

    def test_task_update_view(self):
        self.client.login(username='test', password='qweasdqweasd')
        response = self.client.post(reverse('todo:task_update', args=[self.task.pk]), {
            'title': 'Test Update Task',
            'description': 'Test Update Description',
            'completed': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('todo:task_list'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Test Update Task')
        self.assertEqual(self.task.description, 'Test Update Description')
        self.assertTrue(self.task.completed)


class TaskDeleteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='qweasdqweasd')
        self.task = Task.objects.create(title='Test Title', description='Test Description', user=self.user)

    def test_task_delete_view(self):
        self.client.login(username='test', password='qweasdqweasd')
        response = self.client.post(reverse('todo:task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('todo:task_list'))
        self.assertFalse(Task.objects.filter(title='Test Title'))
