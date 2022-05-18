from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Tasks(models.Model):
    STATUS = [
        {'fulfilled', 'Fulfilled'},
        {'unfulfilled', 'Unfulfilled'}
    ]
    title = models.CharField(verbose_name="Task Name", max_length=255)
    description = models.TextField(verbose_name="Description")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS, default="unfulfilled")
    created_at = models.DateTimeField("Created at", auto_now_add=timezone.now())

    def __str__(self):
        return f'Task:{self.title}'

    @staticmethod
    def get_absolute_url():
        return reverse("tasks")

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
