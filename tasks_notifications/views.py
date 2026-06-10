from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks_notifications/task_list.html'
    context_object_name = 'tasks'
