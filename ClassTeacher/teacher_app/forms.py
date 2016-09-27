from django import forms
from teacher_app.models import TeacherClass


class CreateClassForm(forms.ModelForm):

    class Meta:
        model = TeacherClass
        fields = ('name', 'level',)
