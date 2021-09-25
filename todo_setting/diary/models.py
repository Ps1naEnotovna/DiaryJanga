from django.db import models
from django.utils.timezone import now


class Pupil(models.Model):
    name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    updated_at = models.DateTimeField('Добавление', auto_now=True)

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return self.full_name()

    class Meta:
        db_table = 'pupils'
        verbose_name = 'ученик'
        verbose_name_plural = 'Ученики'


class Subject(models.Model):
    name = models.CharField('Название', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subjects'
        verbose_name = 'предмет'
        verbose_name_plural = 'Предметы'


class Homework(models.Model):
    homework = models.TextField('Домашнее задание')

    def __str__(self):
        return self.homework

    class Meta:
        db_table = 'homework'
        verbose_name = 'домашнее задание'
        verbose_name_plural = 'Домашнее задания'


class Diary(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name='Ученик',
                              on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, verbose_name='Предмет',
                                on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    date = models.DateField('Дата', default=now)
    score = models.IntegerField('Оценка', choices=((5, 5),
                                                        (4, 4),
                                                        (3, 3),
                                                        (2, 2),
                                                        (1, 1)))
    is_present = models.BooleanField('Присутствие', default=False)
    notes = models.TextField('Заметки', null=True, blank=True)
    homework = models.ForeignKey(Homework, verbose_name='Домашнее задание',
                                 on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'diaries'
        verbose_name = 'запись в дневнике'
        verbose_name_plural = 'Записи в дневнике'
