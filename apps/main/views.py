from django.shortcuts import render
from django.views import View

from .models import Announcement


class HomePageView(View):
    def get(self, request):
        announcements = Announcement.objects.all().order_by("-updated_at")
        main_announcement = announcements[0]
        other_announcements = []
        if len(announcements) > 1:
            for i, announcement in enumerate(announcements[1:]):
                announcement.number = i + 2
                other_announcements.append(announcement)

        return render(request, "home_page.html", context={"main_announcement": main_announcement,
                                                          "other_announcements": other_announcements})
