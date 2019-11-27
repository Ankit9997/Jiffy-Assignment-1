from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=80)
    age=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.name
