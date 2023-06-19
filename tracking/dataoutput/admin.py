from django.contrib import admin
from .models import User, Project, Smeta, Director, UserWorkTime, Expenses


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')
    list_display_links = ['name', 'last_name']
    ordering = ['name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'start_date', 'end_date')
    list_display_links = ['name', 'address',  'start_date', 'end_date']
    ordering = ['name']


class SmetaAdmin(admin.ModelAdmin):
    list_display = ('summa', 'date', 'project')
    list_display_links = ('summa', 'date', 'project')
    ordering = ['date']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    list_display_links = ('name',)
    ordering = ['name']


class UserWorkTimeAdmin(admin.ModelAdmin):
    list_display = ('date', 'project', 'user', 'time_work')
    list_display_links = ('date',)
    ordering = ['date']


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'name', 'description', 'summa')
    list_display_links = ('date',)
    ordering = ['date']


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Smeta, SmetaAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(UserWorkTime, UserWorkTimeAdmin)
admin.site.register(Expenses, ExpensesAdmin)
