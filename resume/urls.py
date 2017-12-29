from django.urls import path,re_path,include

from . import views

app_name = "resume"

urlpatterns = [
    re_path('^$',views.Index.as_view(), name="index"),
]