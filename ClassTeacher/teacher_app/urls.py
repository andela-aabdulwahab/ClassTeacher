from django.conf.urls import url
from teacher_app.views import ClassListView, ClassCreateView, ClassDetailView, StudentCreateView

urlpatterns = [
    url(r'^class/$', ClassListView.as_view(), name="class_list"),
    url(r'^class/new/$', ClassCreateView.as_view(), name="class_create"),
    url(r'^class/(?P<pk>[0-9]+)', ClassDetailView.as_view(), name="class_detail"),
    url(r'^students/new/$', StudentCreateView.as_view(), name="student_create"),
]
