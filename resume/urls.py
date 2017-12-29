from django.urls import path,re_path,include
from django.views.generic.base import TemplateView

from . import views

app_name = "resume"

urlpatterns = [
    re_path(r'^$',views.Index.as_view(), name="index"),
    re_path(r'^resume/$', TemplateView.as_view(template_name="resume/resume.html"), name="resume"),
]