from django.shortcuts import render
from django.views import View
from .models import Task, TaskType


class TodoView(View):
    def get(self, request):
        grouped_tasks = [Task.objects.filter(task_type=_type) for _type in TaskType.objects.all()]
        tasks = Task.objects.filter(task_type=None)
        return render(request, 'todo/todo.html', {'tasks': tasks, 'grouped_tasks': grouped_tasks})