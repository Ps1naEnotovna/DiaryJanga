from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import View
from .models import Diary, Pupil, Subject


class DiaryView(View):
    def get(self, request):
        diary = Diary.objects.all()
        return render(request, 'diary/diary.html', {'diaries': diary})


class DiaryPupilGroupView(View):
    def get(self, request):
        group_diary = [Diary.objects.filter(pupil=_pupil) for _pupil in Pupil.objects.all()]
        return render(request, 'diary/diary_pupil_group.html', {'group_diary': group_diary})


class DiarySubjectGroupView(View):
    def get(self, request):
        group_subject_diary = [Diary.objects.filter(subject=_subject) for _subject in
                               Subject.objects.filter(diary__isnull=False).distinct()]
        return render(request, 'diary/diary_subject_group.html', {'group_subject_diary': group_subject_diary})


class DiaryDateGroupView(View):
    def get(self, request: WSGIRequest):
        query = Diary.objects
        if ((order_by := request.GET.get('order_by'))
                and order_by
                in Diary.__doc__[len(Diary.__name__) + 1:-1].split(', ')):
            query = query.order_by(order_by)
        group_date_diary = [query.filter(date=_date)
                            for _date in Diary.objects.all().dates('date', 'day')]
        return render(request,
                      'diary/diary_date_group.html',
                      {'group_date_diary': group_date_diary})


class PupilView(View):
    def get(self, request: WSGIRequest, pupil_id: int):
        query = Diary.objects.filter(pupil_id=pupil_id)
        if ((order_by := request.GET.get('order_by'))
                and order_by
                in Diary.__doc__[len(Diary.__name__) + 1:-1].split(', ')):
            query = query.order_by(order_by)
        group_date_diary = [query.filter(date=_date)
                            for _date in Diary.objects.filter(pupil_id=pupil_id).dates('date', 'day')]
        return render(request,
                      'diary/diary_date_group.html',
                      {'group_date_diary': group_date_diary})
