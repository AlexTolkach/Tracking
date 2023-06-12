from django.db import models
from datetime import datetime


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
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    summa = models.PositiveIntegerField()
    date = models.DateTimeField()
