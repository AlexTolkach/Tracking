from django.db import models
from datetime import datetime


CATEGORIES_OF_EXPENSES = [
    ('w', 'employee benefits'),
    ('b', 'purchase and repair of tools'),
    ('t', 'transport costs')
]


class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Smeta(models.Model):
    summa = models.IntegerField()
    date = models.DateTimeField(auto_created=datetime.now())
    project = models.OneToOneField('Project', on_delete=models.CASCADE)


class Director(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class UserWorkTime(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateTimeField()
    time_work = models.DateTimeField()


class Expenses(models.Model):
    category = models.CharField(max_length=1, choices=CATEGORIES_OF_EXPENSES)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    summa = models.PositiveIntegerField()
    date = models.DateTimeField()
