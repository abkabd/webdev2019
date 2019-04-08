from django.db import models
from datetime import datetime
from django.utils import timezone

class TaskList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    STATUS_CHOICES = (
        ('D', 'DONE'),
        ('U', 'UNDONE'),
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    due_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='UNDONE')
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {} from {} to {} fk={}'.format(self.id, self.name, self.created_at, self.due_on, self.status, self.task_list)


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'task_list_id': self.task_list.name
        }
