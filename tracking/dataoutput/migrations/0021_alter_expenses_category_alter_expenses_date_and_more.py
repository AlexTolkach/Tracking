# Generated by Django 4.2.1 on 2023-07-21 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataoutput', '20_06_2023_0002_alter_director_options_alter_expenses_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='category',
            field=models.CharField(choices=[('w', 'Оплата труда'), ('b', 'покупка и ремонт инструмента'), ('t', 'транспортные расходы'), ('p', 'премии')], max_length=1, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(auto_created=datetime.datetime(2023, 7, 21, 12, 52, 5, 178015), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(auto_created=datetime.datetime(2023, 7, 21, 12, 52, 5, 171017), null=True, verbose_name='Дата завершения проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_created=datetime.datetime(2023, 7, 21, 12, 52, 5, 171017), null=True, verbose_name='Дата начала проекта'),
        ),
        migrations.AlterField(
            model_name='smeta',
            name='date',
            field=models.DateField(auto_created=datetime.datetime(2023, 7, 21, 12, 52, 5, 172017), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='userworktime',
            name='date',
            field=models.DateField(auto_created=datetime.datetime(2023, 7, 21, 12, 52, 5, 175019), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='userworktime',
            name='time_work',
            field=models.IntegerField(verbose_name='Время работы'),
        ),
    ]