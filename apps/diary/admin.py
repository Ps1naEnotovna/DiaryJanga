from django.contrib import admin
from .models import Student, Subject, EducationalSession, TrainingStream, Homework, EducationalMaterial


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ...


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ...


@admin.register(EducationalSession)
class ScheduleAdmin(admin.ModelAdmin):
    ...


@admin.register(TrainingStream)
class TrainingStreamAdmin(admin.ModelAdmin):
    ...


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    ...


@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(admin.ModelAdmin):
    ...