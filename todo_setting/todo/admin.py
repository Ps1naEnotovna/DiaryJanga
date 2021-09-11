from django.contrib import admin
from .models import Task, TaskType


@admin.register(Task)  # связь  между админкой и моделью
class TaskAdmin(admin.ModelAdmin):  # настройки отображения модели в админке
    list_display = ('name', 'text', 'created_at',
                    'updated_at', 'is_solved', 'expected_time',
                    'task_type', 'rating')  # для отображения при выборе задания


@admin.register(TaskType)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at', 'rating')
