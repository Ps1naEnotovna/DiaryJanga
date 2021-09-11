"""todo_setting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import TodoView
from diary.views import DiaryView, DiaryPupilGroupView, DiarySubjectGroupView, DiaryDateGroupView, PupilView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo',  TodoView.as_view()),
    path('diary', DiaryView.as_view()),
    path('group_diary', DiaryPupilGroupView.as_view()),
    path('group_subject_diary', DiarySubjectGroupView.as_view()),
    path('group_date_diary', DiaryDateGroupView.as_view()),
    path('diary/pupil/<int:pupil_id>', PupilView.as_view(), name='pupil')
    ]
