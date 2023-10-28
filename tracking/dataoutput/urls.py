from django.urls import path
from .views import home_page, projects_list

urlpatterns = [
    path('home', home_page),
    path('projects', projects_list, name='projects')
]
