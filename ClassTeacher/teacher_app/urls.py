from django.conf.urls import url
from teacher_app.views import ClassListView, ClassCreateView
urlpatterns = [
    url(r'^class/$', ClassListView.as_view(), name="class_list"),
    url(r'^class/new/$', ClassCreateView.as_view(), name="class_create")
]
