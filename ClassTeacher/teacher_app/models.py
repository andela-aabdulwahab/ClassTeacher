from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(blank=False)
    last_name = models.CharField(blank=False)
    middle_name = models.CharField(blank=True)
    age = models.IntegerField(blank=True)
    class_name = models.ForeignKey(Student, related_name="students")


class TeacherClass(models.Model):
    LEVEL = (
        ('Primary one', 'Primary one'),
        ('Primary Two', 'Primary Two'),
        ('Primary Three', 'Primary Three')
    )
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, related_name="classes")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=20, choices=LEVEL, null=False, default="Primary one")

    def get_aboslute_url(self):
        return reverse('class:class_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['date_created']
