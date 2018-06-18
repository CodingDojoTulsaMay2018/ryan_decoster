from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name should be at least 5 characters.'
        if len(postData['desc']) < 15:
            errors['desc'] = 'Description should be at least 15 characters.'
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Course: {}|{} {}>".format(self.id, self.name, self.desc)

    objects = CourseManager()
