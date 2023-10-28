from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Project


def home_page(request):
    return render(request, 'home.html')


def projects_list(request):
    context = {
        "projects": Project.objects.all()
    }
    return render(request, "projects.html", context=context)
