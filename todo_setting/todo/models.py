from django.db import models


class TaskType(models.Model):
    name = models.CharField('Название', max_length=32)
    rating = models.IntegerField('Рейтинг', default=0)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_types'
        verbose_name = 'тип задачи'
        verbose_name_plural = 'Типы задачи'


class Task(models.Model):
    name = models.CharField('Название', max_length=64)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    is_solved = models.BooleanField('Решено?', default=False)
    expected_time = models.DateTimeField('Ожидаемое время решения')
    task_type = models.ForeignKey(TaskType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    rating = models.IntegerField('Рейтинг', default=0)

    def __str__(self):
        return self.name + (' 🌝' if self.is_solved else ' 🌚')

    class Meta:
        db_table = 'tasks'
        verbose_name = 'задачу'
        verbose_name_plural = 'Задачи'
