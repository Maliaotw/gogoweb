from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

from django.test import TestCase
from rest_framework.test import APIClient
import json


class ReadUserTest(APITestCase):
    def setUp(self):
        self.task_obj = Task.objects.create(name="買晚餐")

    def test_can_read_task_list(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_task_detail(self):
        response = self.client.get(reverse('task-detail', args=[self.task_obj.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateUserTest(APITestCase):
    def setUp(self):
        self.data = {'name': '買晚餐'}

    def test_can_create_user(self):
        response = self.client.post(reverse('task-list'),self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.task_obj = Task.objects.create(name="買早餐")
        self.data = {'name': '買早餐', 'status': 1, 'id': self.task_obj.id}

    def test_can_update_user(self):
        response = self.client.put(reverse('task-detail', args=[self.task_obj.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.task_obj = Task.objects.create(name="買晚餐")

    def test_can_delete_user(self):
        response = self.client.delete(reverse('task-detail', args=[self.task_obj.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

