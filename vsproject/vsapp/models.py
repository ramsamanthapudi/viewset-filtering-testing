from django.db import models

# Create your models here.


class Student(models.Model):
    Name = models.CharField(max_length=47)
    age = models.IntegerField()
    place = models.CharField(max_length=47)
    department = models.CharField(max_length=9)
