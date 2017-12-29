from django.urls import path,re_path,include
from django.views.generic.base import TemplateView

from . import views

app_name = "resume"

urlpatterns = [
    path('',TemplateView.as_view(template_name="resume/index.html"), name="index"),
    path('resume/', TemplateView.as_view(template_name="resume/resume.html"), name="resume"),
    path('projects/',TemplateView.as_view(template_name="resume/project.html"), name="project"),
]