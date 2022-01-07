from django.db import models
from django.utils.timezone import now

from ..accordant_utils.base_model import CUDateModel


class Announcement(CUDateModel):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'announcement'
        verbose_name = 'объявление'
        verbose_name_plural = 'Объявления'


class Training(models.Model):
    letter = models.IntegerField('Буква', choices=('А', 'Б', 'В', 'Г'))
    number = models.IntegerField('Цифра', choices=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

    def full_name_training(self):
        return f'{self.number}{self.letter}'

    def __str__(self):
        return self.full_name_training()

    class Meta:
        db_table = 'training'
        verbose_name = 'поток'
        verbose_name_plural = 'Потоки'


class Student(CUDateModel):
    name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    training = models.ForeignKey(Training, verbose_name='Поток',
                                 on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return self.full_name()

    class Meta:
        db_table = 'student'
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


class Homework(CUDateModel):
    homework = models.TextField('Домашнее задание')
    subject = models.ForeignKey(Subject, verbose_name='Предмет',
                                on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.homework

    class Meta:
        db_table = 'homework'
        verbose_name = 'домашнее задание'
        verbose_name_plural = 'Домашнее задания'


class Schedule(models.Model):
    student = models.ForeignKey(Student, verbose_name='Ученик',
                                on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, verbose_name='Предмет',
                                on_delete=models.CASCADE, null=True)
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
