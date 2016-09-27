from django.shortcuts import render
from django.views.generic.list import ListView
from teacher_app.models import TeacherClass
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ClassListView(LoginRequiredMixin, ListView):
    template_name = 'teacher_app/class_list.html'
    queryset = TeacherClass.objects.all()
