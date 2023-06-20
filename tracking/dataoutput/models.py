from django.db import models
from datetime import datetime


CATEGORIES_OF_EXPENSES = [
    ('w', 'employee benefits'),
    ('b', 'purchase and repair of tools'),
    ('t', 'transport costs')
]


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')

    class Meta:
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    start_date = models.DateField(
        auto_created=datetime.now(), null=True, verbose_name='Дата начала проекта'
    )
    end_date = models.DateField(
        auto_created=datetime.now(), null=True, verbose_name='Дата завершения проекта'
    )

    class Meta:
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Smeta(models.Model):
    summa = models.IntegerField(verbose_name='Сумма')
    date = models.DateField(auto_created=datetime.now(), verbose_name='Дата')
    project = models.OneToOneField('Project', on_delete=models.CASCADE, verbose_name='Проект')

    class Meta:
        verbose_name_plural = 'Сметы'


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Проект')

    class Meta:
        verbose_name_plural = 'Директора'

    def __str__(self):
        return self.name


class UserWorkTime(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Проект')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Работник')
    date = models.DateField(auto_created=datetime.now(), verbose_name='Дата')
    time_work = models.PositiveIntegerField(verbose_name='Время работы')

    class Meta:
        verbose_name_plural = 'Время работы'


class Expenses(models.Model):
    category = models.CharField(max_length=1, choices=CATEGORIES_OF_EXPENSES, verbose_name='Категория')
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')
    summa = models.FloatField(verbose_name='Сумма')
    date = models.DateField(auto_created=datetime.now(), verbose_name='Дата')

    class Meta:
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return self.name
