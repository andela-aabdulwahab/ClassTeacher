from django import forms
from teacher_app.models import TeacherClass, Student


class CreateClassForm(forms.ModelForm):

    class Meta:
        model = TeacherClass
        fields = ('name', 'level',)


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'age', 'class_name')
