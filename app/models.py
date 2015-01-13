from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)

class Household(models.Model):
    students = models.ManyToManyField(Student, through='StudentHousehold')

class StudentHousehold(models.Model):
    household = models.ForeignKey(Household)
    student = models.ForeignKey(Student)
    primary = models.BooleanField(default=False)
