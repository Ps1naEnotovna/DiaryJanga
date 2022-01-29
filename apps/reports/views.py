from django.shortcuts import render
from django.views import View


class ReportView(View):
    def get(self, request):
        return render(request, "report.html")
