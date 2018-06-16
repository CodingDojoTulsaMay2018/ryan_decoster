from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 5:
            errors['first_name'] = 'First name should be at least 5 characters.'
        if len(postData['last_name']) < 5:
            errors['last_name'] = 'Last name should be at least 5 characters.'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Email is not valid.'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User: {}|{} {} {}>".format(self.id, self.first_name, self.last_name, self.email)

    objects = UserManager()