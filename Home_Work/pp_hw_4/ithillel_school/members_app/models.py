from django.db import models
from courses_app.models import Course


class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name
