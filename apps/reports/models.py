from django.db import models

# Create your models here.
from django.utils.timezone import now

from apps.diary.models import Student


class Report(models.Model):
    date = models.DateField('Дата', default=now)
    student = models.ForeignKey(Student, verbose_name='Ученик',
                                on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'reports'
        verbose_name = 'отчёт'
        verbose_name_plural = 'Отчёты'