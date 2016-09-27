from django.conf.urls import url
from teacher_app.views import ClassListView
urlpatterns = [
    url(r'^class/$', ClassListView.as_view(), name="class_list"),
]
