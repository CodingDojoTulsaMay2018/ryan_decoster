
from __future__ import unicode_literals
from django.db import models

# class ItemManager(models.Manager):
#     def validator(self, postData):
#         errors = {}
#         if len(postData['name']) < 5:
#             errors['name'] = 'Course name should be at least 5 characters.'
#         if len(postData['desc']) < 15:
#             errors['desc'] = 'Description should be at least 15 characters.'
#         return errors


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __repr__(self):
        return "<Item: {}|{} {}>".format(self.id, self.name, self.price)

