from django.contrib import admin
from .models import Diary, Subject, Pupil


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('pupil', 'subject', 'created_at', 'score', 'is_present', 'notes', 'updated_at', 'date')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'updated_at')
