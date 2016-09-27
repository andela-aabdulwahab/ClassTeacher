from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TeacherClass(models.Model):
    teacher = models.ForeignKey(User, related_name="classes")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
