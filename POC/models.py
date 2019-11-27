# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Registration(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other','Other'),
    )
    name=models.CharField(max_length=80)
    age=models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    address=models.TextField(default='')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    zip=models.age=models.IntegerField(null=True)


    def __str__(self):
        return self.name





    def get_absolute_url(self):
        return reverse('person_changelist')
