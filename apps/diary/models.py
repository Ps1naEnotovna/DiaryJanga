from django.db import models
from django.utils.timezone import now
from apps.accordant_utils.base_model import CUDateModel


class TrainingStream(models.Model):
    letter = models.CharField('Буква', choices=(('А', 'A'),
                                                ('Б', 'Б'),
                                                ('В', 'В'),
                                                ('Г', 'Г')), max_length=1)
    number = models.IntegerField('Цифра', choices=[(a, a) for a in range(1, 12)])

    def full_name_training(self):
        return f'{self.number}{self.letter}'

    def __str__(self):
        return self.full_name_training()

    class Meta:
        db_table = 'training_streams'
        verbose_name = 'поток'
        verbose_name_plural = 'Потоки'


class Student(CUDateModel):
    name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    training = models.ForeignKey(TrainingStream, verbose_name='Поток',
                                 on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return self.full_name()

    class Meta:
        db_table = 'students'
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


class EducationalSession(models.Model):
    training_stream = models.ForeignKey(TrainingStream, verbose_name='Поток',
                                        on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, verbose_name='Предмет',
                                on_delete=models.CASCADE, null=True)
    date = models.DateField('Дата', default=now)
    notes = models.TextField('Заметки', null=True, blank=True)
    homework = models.ForeignKey(Homework, verbose_name='Домашнее задание',
                                 on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'educational_sessions'
        verbose_name = 'учебная сессия'
        verbose_name_plural = 'Учебные сессии'


class EducationalMaterial(CUDateModel):
    subject = models.ForeignKey(Subject, verbose_name='Предмет',
                                on_delete=models.CASCADE, null=True)
    text = models.TextField('Текст', null=True, blank=True)
    training_stream_number = models.IntegerField('Цифра потока', choices=[(a, a) for a in range(1, 12)])
    available_after = models.ForeignKey('self', verbose_name='Доступно после прохождения материала номер',
                                        on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'educational_materials'
        verbose_name = 'учебный материал'
        verbose_name_plural = 'Учебные материалы'


class Score(CUDateModel):
    student = models.ForeignKey(Student, verbose_name='Ученик',
                                on_delete=models.CASCADE, null=True)
    schedule = models.ForeignKey(EducationalSession, verbose_name='',
                                 on_delete=models.CASCADE, null=True)
    score = models.IntegerField('Оценка', choices=[(a, a) for a in range(5, 0, -1)])
    is_present = models.BooleanField('Присутствие', default=False)

    class Meta:
        db_table = 'scores'
        verbose_name = 'оценка'
        verbose_name_plural = 'Оценки'