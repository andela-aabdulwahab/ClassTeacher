from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from teacher_app.models import TeacherClass
from teacher_app.forms import CreateClassForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ClassListView(LoginRequiredMixin, ListView):
    template_name = 'teacher_app/class_list.html'
    queryset = TeacherClass.objects.all()


class ClassCreateView(LoginRequiredMixin, CreateView):
    template_name = 'teacher_app/class_create.html'
    form_class = CreateClassForm
