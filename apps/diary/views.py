from django.shortcuts import render
from django.views import View


class DiaryView(View):
    def get(self, request):
        return render(request, "diary.html")
